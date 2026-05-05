from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__multilinear_model_marc_hardening_rule import (
    OneOf_MultilinearModelMarcHardeningRule,
)


class MultilinearModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MULTILINEAR",
        description="Schema name: MultilinearModelMarc",
    )
    stress_strain_curve: DimensionalFunction_Pressure | None = Field(
        validation_alias="stressStrainCurve", serialization_alias="stressStrainCurve", default=None
    )
    hardening_rule: OneOf_MultilinearModelMarcHardeningRule | None = Field(
        validation_alias="hardeningRule", serialization_alias="hardeningRule", default=None
    )
