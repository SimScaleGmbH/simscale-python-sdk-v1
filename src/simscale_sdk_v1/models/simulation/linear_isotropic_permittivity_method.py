from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class LinearIsotropicPermittivityMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LINEAR_ISOTROPIC",
        description="Schema name: LinearIsotropicPermittivityMethod",
    )
    relative_electric_permittivity: float | None = Field(
        validation_alias="relativeElectricPermittivity", serialization_alias="relativeElectricPermittivity", default=1.0
    )
