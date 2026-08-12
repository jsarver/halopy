# export.py
from typing import Any, Dict, Callable

from pydantic import BaseModel


def flatten_model(
    model: BaseModel,
    *,
    nested_attr: str = "fields",
    prefix: str = "cf_",
    include: set[str] | None = None,
    exclude: set[str] | None = None,
) -> dict[str, Any]:
    data = model.model_dump(exclude={nested_attr})

    for item in getattr(model, nested_attr, None) or []:
        if item.name is None:
            continue
        data[f"{prefix}{item.name}"] = item.value

    if include is not None:
        data = {k: v for k, v in data.items() if k in include}
    if exclude is not None:
        data = {k: v for k, v in data.items() if k not in exclude}

    return data

def flatten_dict(
    data: Dict[str, Any],
    nested_field: str = "fields",
    nested_key:str = "name",
    nested_value:str = "value",
    include: set[str] | None = None,
    exclude: set[str] | None = None,
) -> dict[str, Any]:
    flat_dict = data.copy()
    
    for field in flat_dict.pop(nested_field) or []:
        try:
            flat_dict[field[nested_key]] = field.get(nested_value)
        except KeyError:
            print(flat_dict, field)
    if include is not None:
        lower_include = [col.lower() for col in include]
        flat_dict = {k: v for k, v in flat_dict.items() if k.lower() in lower_include}
    if exclude is not None:
        lower_exclude = [col.lower() for col in exclude]
        flat_dict = {k: v for k, v in flat_dict.items() if k.lower() not in lower_exclude}

    return flat_dict