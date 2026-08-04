from typing import Any


class FlattenFieldsMixin:
    """
    Mixin for Models with a nest fields attribute
    Allows the fields to be flattened as attributes in the main class primarily for exporting data
    """
    def to_flat_dict(
        self,
        *,
        include: set[str] | None = None,
        exclude: set[str] | None = None,
    ) -> dict[str, Any]:

        # start with normal attributes
        data = self.model_dump(exclude={"fields"})

        # overlay custom fields
        for field in getattr(self, "fields", []) or []:
            data[field.name] = field.value

        #adding all included fields, if specified
        if include is not None:
            data = {k: v for k, v in data.items() if k in include}

        # adding all fields but the excluded, if specified
        if exclude is not None:
            data = {k: v for k, v in data.items() if k not in exclude}

        return data