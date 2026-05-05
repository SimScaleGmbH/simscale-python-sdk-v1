from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__inv_pressure import Dimensional_InvPressure
from simscale_sdk_v1.models.simulation.one_of__ogden_hyper_elastic_model_order import OneOf_OgdenHyperElasticModelOrder


class OgdenHyperElasticModel(SimScaleModel):
    """Choose the hyperelastic material model that should be used. All models derive the stress-strain relation from a strain energy function defined by the material model parameters."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OGDEN",
        description="Choose the hyperelastic material model that should be used. All models derive the stress-strain relation from a strain energy function defined by the material model parameters.  Schema name: OgdenHyperElasticModel",
    )
    order: OneOf_OgdenHyperElasticModelOrder | None = Field(default=None)
    d1: Dimensional_InvPressure | None = Field(default=None)
