from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__bilinear_elasto_plastic_model_hardening_model import (
    OneOf_BilinearElastoPlasticModelHardeningModel,
)
from simscale_sdk_v1.models.simulation.one_of__bilinear_elasto_plastic_model_poissons_ratio import (
    OneOf_BilinearElastoPlasticModelPoissonsRatio,
)


class BilinearElastoPlasticModel(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BILINEAR",
        description="Schema name: BilinearElastoPlasticModel",
    )
    youngs_modulus: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulus", serialization_alias="youngsModulus", default=None
    )
    poissons_ratio: OneOf_BilinearElastoPlasticModelPoissonsRatio | None = Field(
        validation_alias="poissonsRatio", serialization_alias="poissonsRatio", default=None
    )
    hardening_model: OneOf_BilinearElastoPlasticModelHardeningModel | None = Field(
        validation_alias="hardeningModel", serialization_alias="hardeningModel", default=None
    )
