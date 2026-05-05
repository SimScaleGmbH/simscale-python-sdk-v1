from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class ArrudaBoycePlasticElastoplasticNetwork(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ARRUDA_BOYCE_PLASTIC",
        description="Schema name: ArrudaBoycePlasticElastoplasticNetwork",
    )
    nk_theta: Dimensional_Pressure | None = Field(
        validation_alias="nkTheta", serialization_alias="nkTheta", default=None
    )
    chain_length: float | None = Field(
        validation_alias="chainLength",
        serialization_alias="chainLength",
        default=None,
        description='Defined by the number of statistically independent links (N) in a polymer chain, this determines the material\'s extensibility. It dictates the "locking stretch" point where chains become fully extended and the stress-strain curve turns sharply upward.',
    )
    yield_stress: Dimensional_Pressure | None = Field(
        validation_alias="yieldStress", serialization_alias="yieldStress", default=None
    )
    tangent_modulus: Dimensional_Pressure | None = Field(
        validation_alias="tangentModulus", serialization_alias="tangentModulus", default=None
    )
    kinematic_fraction: float | None = Field(
        validation_alias="kinematicFraction",
        serialization_alias="kinematicFraction",
        default=None,
        description="This value (from 0 to 1) defines the weight of the kinematic component relative to the isotropic component for the combined hardening rule. A value of 1 represents pure kinematic hardening, while 0 represents pure isotropic hardening.",
    )
