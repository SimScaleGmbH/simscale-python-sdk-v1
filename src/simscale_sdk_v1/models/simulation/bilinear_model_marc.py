from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.one_of__bilinear_model_marc_hardening_model import (
    OneOf_BilinearModelMarcHardeningModel,
)
from simscale_sdk_v1.models.simulation.one_of__bilinear_model_marc_hardening_rule import (
    OneOf_BilinearModelMarcHardeningRule,
)


class BilinearModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BILINEAR",
        description="Schema name: BilinearModelMarc",
    )
    yield_stress: Dimensional_Pressure | None = Field(
        validation_alias="yieldStress", serialization_alias="yieldStress", default=None
    )
    hardening_model: OneOf_BilinearModelMarcHardeningModel | None = Field(
        validation_alias="hardeningModel", serialization_alias="hardeningModel", default=None
    )
    hardening_rule: OneOf_BilinearModelMarcHardeningRule | None = Field(
        validation_alias="hardeningRule", serialization_alias="hardeningRule", default=None
    )
