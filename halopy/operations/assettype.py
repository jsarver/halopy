"""Asset type helper functions
"""
from __future__ import annotations
from dataclasses import dataclass
from halopy.paths import Assettype

# Tab settings copied between asset types. Identity fields
# (id, entity_id, tab_id) are never copied; sequence is recomputed.
DEFAULT_TAB_SETTINGS: tuple[str, ...] = ("display", "nosidemenu", "icon")

def get_assettype(client, assettype_id: int) -> dict:
    """Return a single asset type with full details as a dict."""
    return client.get(Assettype, id=assettype_id, includedetails=True).json()


def assettype_id(client, name: str) -> int:
    """Return the id of the asset type with this name (case-insensitive, exact)."""
    all_types = client.list(Assettype).json()
    matches = [t for t in all_types if t["name"].casefold() == name.casefold()]
    if not matches:
        raise LookupError(f"No asset type named {name!r}")
    if len(matches) > 1:
        raise LookupError(f"Asset type name {name!r} is ambiguous: ids {[t['id'] for t in matches]}")
    return matches[0]["id"]


@dataclass
class TabLayoutPlan:
    """A planned tab_config write, produced by copy_tab_layout.

    tab_config is the full payload in final order. The three name lists
    summarize the plan for inspection during a dry run.
    """

    target_assettype_id: int
    tab_config: list[dict]
    mirrored: list[str]  # on both types: reordered and restyled
    skipped: list[str]  # on source only: cannot be copied
    extras: list[str]  # on target only: kept, moved to the end


def by_sequence(tab):
    return tab.get("sequence", float("inf"))


def copy_tab_layout(client, source_assettype_id: int, target_assettype_id: int,
        settings: tuple[str, ...] = DEFAULT_TAB_SETTINGS, sequence_step: int = 10,
        dry_run: bool = True, ) -> TabLayoutPlan:
    """Make the target asset type's tabs match the source's order and settings.

    In one sentence: arrange the target's own tab rows in the source's
    order, copy each one's display settings from its source twin, park
    target-only tabs at the end, and renumber everything.

    Tabs are paired by tab_id. Target rows keep their identity fields
    (id, entity_id, tab_id). Source-only tabs are reported, never created.

    With dry_run=True (default) nothing is written; inspect the returned
    plan, then pass it to apply_tab_layout (or rerun with dry_run=False).
    """
    source_tabs = sorted(get_assettype(client, source_assettype_id)["tab_config"], key=by_sequence)
    target_tabs = sorted(get_assettype(client, target_assettype_id)["tab_config"], key=by_sequence)

    # Pair each source tab with the target tab that has the same tab_id.
    target_by_id = {tab["tab_id"]: tab for tab in target_tabs}
    pairs = [(source_tab, target_by_id[source_tab["tab_id"]]) for source_tab in source_tabs if
        source_tab["tab_id"] in target_by_id]

    # Copy the display settings from each source tab onto its target twin.
    for source_tab, target_tab in pairs:
        for key in settings:
            if key in source_tab:
                target_tab[key] = source_tab[key]

    # New layout: target's twins in source order, then target-only extras.
    source_ids = {tab["tab_id"] for tab in source_tabs}
    mirrored = [target_tab for _, target_tab in pairs]
    extras = [tab for tab in target_tabs if tab["tab_id"] not in source_ids]
    skipped = [tab for tab in source_tabs if tab["tab_id"] not in target_by_id]

    new_layout = mirrored + extras
    for position, tab in enumerate(new_layout, start=1):
        tab["sequence"] = position * sequence_step

    plan = TabLayoutPlan(target_assettype_id=target_assettype_id, tab_config=new_layout,
        mirrored=[tab["tab_name"] for tab in mirrored], skipped=[tab["tab_name"] for tab in skipped],
        extras=[tab["tab_name"] for tab in extras], )
    if not dry_run:
        apply_tab_layout(client, plan)
    return plan


def apply_tab_layout(client, plan: TabLayoutPlan) -> None:
    """Write a TabLayoutPlan's tab_config to its target asset type."""
    client.create(Assettype, json=[{"id": plan.target_assettype_id, "tab_config": plan.tab_config}], )


def generate_assettype_fields(client):
    at_dict = []
    for a in client.list(Assettype).json():
        group = a['assetgroup_name']
        assettype = a['name']
        detail_display = a['asset_details_tab_display']
        for f in a['fields']:
            tab = f.get('tab_name', "missing")
            tab_group = f.get('groupname', "missing")
            at_dict.append({"group": group, "assettype": assettype, "asset_field": f['field_name'],
                            'details_display': detail_display, "tab": tab, "tab_group": tab_group})
    return at_dict
