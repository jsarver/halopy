# ui/resources.py
import halopy.api.paths as paths
from halopy.api.paths import Endpoint

def find_resources() -> dict[str, type]:
    resources = {}
    for name, obj in vars(paths).items():
        if not isinstance(obj, type) or obj is Endpoint:
            continue
        ops = {k for k, v in vars(obj).items() if isinstance(v, Endpoint)}
        if "LIST" in ops:  # only objects the table can actually load
            resources[name] = obj
    return resources


RESOURCES = find_resources()