import json
import sys

from nicegui import ui, run
from halopy.client import HaloClient
from halopy.api.core import list_record
from halopy.resources import RESOURCES
from itertools import batched
import argparse

BATCH_SIZE = 50
READ_ONLY = {"id"}  # fields you never want to edit
state = {"resource": None, "name": None, "all_columns": [], "params": {}}
# Spell these exactly as they appear in paths.py (your request() matches on k.lower())
FULL_DETAIL_FLAGS = {"includecustomfields", "includeassetfields", "showall"}

def full_detail_params(resource):
    return {p: True for p in resource.GET.query_params if p in FULL_DETAIL_FLAGS}

def get_full(record_id):
    resource = state["resource"]
    resp = client.get(resource, id=record_id, **full_detail_params(resource))
    return resp.json()

def is_simple(value) -> bool:
    return not isinstance(value, (dict, list))

def make_input(key, value):
    if isinstance(value, bool):
        return ui.checkbox(key, value=value)
    if isinstance(value, (int, float)):
        return ui.number(key, value=value)
    if not is_simple(value):
        ui.label(f"{key}: {value}").classes("text-gray-500")  # show nested data, read-only
        return None
    return ui.input(key, value="" if value is None else str(value))

def convert(text, original):
    if isinstance(original, bool):
        return text.strip().lower() in ("true", "1", "yes")
    if isinstance(original, int):
        return int(text)
    if isinstance(original, float):
        return float(text)
    if original is None and text == "":
        return None
    return text

def read_value(widget, original):
    """Convert the widget value back to the original type so comparisons work."""
    v = widget.value
    if isinstance(original, int) and not isinstance(original, bool) and v is not None:
        return int(v)  # ui.number returns floats
    if original is None and v == "":
        return None
    return v


def update_local_row(record_id, changes):
    row = next(r for r in table.rows if r["id"] == record_id)
    row.update(changes)
    table.update()

def save_records(payload: list[dict]):
    """Send a list of updated records to Halo in one call."""
    return client.create(state["resource"], json=payload)

async def open_edit():
    if len(table.selected) != 1:
        ui.notify("Select exactly one row to edit")
        return
    record = await run.io_bound(get_full, table.selected[0]["id"])
    inputs = {}

    with ui.dialog() as dialog, ui.card().classes("w-96"):
        ui.label(f"Record {record['id']}").classes("text-lg")
        for key, value in record.items():
            if key in READ_ONLY:
                continue
            widget = make_input(key, value)
            if widget is not None:
                inputs[key] = widget

        async def save():
            changes = {}
            for key, widget in inputs.items():
                new = read_value(widget, record[key])
                if new != record[key]:
                    changes[key] = new
            if not changes:
                ui.notify("No changes")
                return
            payload = [{"id": int(record["id"]), **changes}]
            await run.io_bound(save_records, payload)
            update_local_row(record["id"], changes)
            ui.notify(f"Updated: {', '.join(changes)}")
            dialog.close()

        with ui.row():
            ui.button("Save", on_click=save)
            ui.button("Cancel", on_click=dialog.close).props("flat")
    dialog.open()

async def open_bulk():
    selected = list(table.selected)
    if not selected:
        ui.notify("Select at least one row")
        return
    sample = await run.io_bound(get_full, selected[0]["id"])
    editable_fields = sorted(k for k, v in sample.items() if is_simple(v) and k not in READ_ONLY)

    with ui.dialog() as dialog, ui.card().classes("w-96"):
        ui.label(f"Bulk update {len(selected)} records").classes("text-lg")
        field = ui.select(editable_fields, label="Field")   # this line was lost
        value = ui.input("New value")
        status = ui.label("test")

        async def apply():
            if not field.value:
                ui.notify("Pick a field")
                return
            payload = [
                {"id": int(row["id"]), field.value: convert(value.value, sample.get(field.value))}
                for row in selected
            ]
            done, failed=0,[]
            for batch in batched(payload,BATCH_SIZE):
                batch = list(batch)
                try:
                    await run.io_bound(save_records, batch)

                except Exception as e:
                    failed.append(f"ids {batch[0]['id']}–{batch[-1]['id']}: {e}")
                    continue
                for item in batch:
                    update_local_row(item["id"],{field.value: item[field.value]})
                done+=len(batch)
                status.text = f"{done}/{len(selected)} updated"
            if failed:
                ui.notify(f"{len(failed)} batch(es) failed, see console", type="warning")
                print("\n".join(failed))
            else:
                ui.notify(f"Updated {done} records",type="positive")
                dialog.close()


        with ui.row():
            ui.button("Apply", on_click=apply)
            ui.button("Cancel", on_click=dialog.close).props("flat")
    dialog.open()

def set_visible(names):
    names = set(names or [])
    # Filtering the full list keeps the original column order
    table.columns = [c for c in state["all_columns"] if c["name"] in names]
    table.update()

def refresh_param_chips():
    param_chips.clear()
    with param_chips:
        for k, v in state["params"].items():
            ui.button(f"{k}={v}", icon="close",
                      on_click=lambda k=k: remove_param(k)).props("flat dense no-caps")


def add_param():
    if not param_name.value:
        ui.notify("Pick a filter")
        return
    state["params"][param_name.value] = param_value.value
    param_value.value = ""
    refresh_param_chips()


def remove_param(k):
    state["params"].pop(k, None)
    refresh_param_chips()


async def apply_params():
    await load(state["name"], **state["params"])

async def load(name, **params):  # NEW
    resource = RESOURCES[name]
    state["resource"] = resource
    state["name"] = name
    state["params"] = dict(params)
    refresh_param_chips()

    param_name.options = sorted(resource.LIST.query_params)
    param_name.value = None
    param_name.update()
    rows = await run.io_bound(list_record, client, resource, **params) or []
    fields = [k for k, v in rows[0].items() if is_simple(v)] if rows else []

    state["all_columns"] =[{"name":k,"label":k,"field":k,"sortable":True} for k in fields]

    table.rows = rows
    table.selected = []
    col_picker.options =fields
    col_picker.value= fields
    col_picker.update()
    set_visible(fields)

with ui.row().classes("items-center"):
    ui.select(  # NEW
        sorted(RESOURCES), value="Asset", label="Object",
        with_input=True, on_change=lambda e: load(e.value),
    )
    search = ui.input("Search")
    ui.button("Edit", on_click=open_edit)
    ui.button("Bulk update", on_click=open_bulk)

with ui.row().classes("items-center w-full"):
    col_picker = ui.select(
        [], multiple=True, label="Columns", with_input=True,
        on_change=lambda e: set_visible(e.value),
    ).props("use-chips").classes("min-w-[300px] grow")
    ui.button("All", on_click=lambda: col_picker.set_value(list(col_picker.options))).props("flat")
    ui.button("None", on_click=lambda: col_picker.set_value([])).props("flat")

with ui.row().classes("items-center w-full"):
    param_name = ui.select([], label="Filter", with_input=True).classes("min-w-[200px]")
    param_value = ui.input("Value").on("keydown.enter", add_param)
    ui.button("Add", on_click=add_param).props("flat")
    ui.button("Apply", on_click=apply_params)
    param_chips = ui.row().classes("items-center")

with ui.right_drawer(value=False).props("width=450 bordered") as drawer:
    detail = ui.column().classes("w-full")

table = ui.table(
    columns=[], rows=[], row_key="id",
    selection="multiple", pagination=25,
).classes("w-full")
async def show_detail(e):
    row = e.args[1]
    record = await run.io_bound(get_full, row["id"])
    detail.clear()
    with detail:
        with ui.row().classes("items-center justify-between w-full"):
            ui.label(f"{state['name']} {row['id']}").classes("text-lg")
            ui.button(icon="close", on_click=drawer.hide).props("flat dense")
        for k, v in record.items():
            if is_simple(v):
                ui.label(f"{k}: {v}")
            else:
                ui.label(k).classes("font-bold")
                ui.code(json.dumps(v, indent=2), language="json").classes("w-full")
    drawer.show()

table.on("rowClick", show_detail)
search.bind_value(table, "filter")
ui.timer(0, lambda: load("Asset", pageinate=True, page_no=10, assetgroup_id=101), once=True)



parser = argparse.ArgumentParser()
parser.add_argument('--config')
args = parser.parse_args()

client = HaloClient.from_env_file(args.config)

ui.run(title="Halo Toolkit")