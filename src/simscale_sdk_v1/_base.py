"""Base model and oneOf dispatch helper for generated models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class SimScaleModel(BaseModel):
    """Base class for all generated SimScale models."""

    model_config = ConfigDict(
        populate_by_name=True,
        # Serialize using camelCase aliases by default
        serialize_by_alias=True,
    )


def parse_discriminated_union(
    value: Any,
    *,
    disc_key: str,
    variants: dict[str, type],
) -> Any:
    """BeforeValidator for oneOf: dispatch on discriminator key.

    If *value* is already a model instance, return as-is.
    If it's a dict, look up the discriminator value and validate via the matching variant class.
    """
    if isinstance(value, BaseModel):
        return value
    if isinstance(value, dict):
        disc_value = value.get(disc_key)
        variant_cls = variants.get(disc_value)
        if variant_cls is not None:
            return variant_cls.model_validate(value)
        raise ValueError(
            f"Unknown discriminator value {disc_value!r} for key {disc_key!r}. Known values: {sorted(variants.keys())}"
        )
    return value
