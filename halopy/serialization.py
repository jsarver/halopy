# export.py
from typing import Any

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