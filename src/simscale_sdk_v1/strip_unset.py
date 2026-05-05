"""Strip optional fields the user didn't explicitly set, preventing them from being serialized.

The SimScale API uses conditional validation — sending an optional field whose condition
isn't met causes a 400 error.  This function uses Pydantic's ``model_fields_set`` to null
out *optional* (allows-None) fields the user didn't explicitly set.  Non-optional fields
with defaults (e.g. ``version: str = "34.0"``) are left intact because the API requires them.

Used together with ``model_dump(exclude_none=True)`` in the client, the nulled-out fields
are omitted from the JSON payload.
"""

from __future__ import annotations

import types
from typing import Union, get_args, get_origin

from pydantic import BaseModel


def _field_allows_none(field_info) -> bool:
    annotation = field_info.annotation
    if annotation is type(None):
        return True
    origin = get_origin(annotation)
    if origin is Union or origin is types.UnionType:
        return type(None) in get_args(annotation)
    return False


def strip_unset_defaults(model):
    """Recursively null out optional fields that weren't explicitly set."""
    if not isinstance(model, BaseModel):
        return model
    for field_name, field_info in type(model).model_fields.items():
        if field_name == "type_":  # Never strip discriminator field
            continue
        if field_name not in model.model_fields_set:
            if _field_allows_none(field_info) and getattr(model, field_name) is not None:
                object.__setattr__(model, field_name, None)
        else:
            val = getattr(model, field_name)
            if isinstance(val, BaseModel):
                strip_unset_defaults(val)
            elif isinstance(val, list):
                for item in val:
                    if isinstance(item, BaseModel):
                        strip_unset_defaults(item)
    return model
