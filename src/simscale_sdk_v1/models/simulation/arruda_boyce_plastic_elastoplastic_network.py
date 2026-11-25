from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__arruda_boyce_plastic_elastoplastic_network_chain_length_function import (
    OneOf_ArrudaBoycePlasticElastoplasticNetworkChainLengthFunction,
)


class ArrudaBoycePlasticElastoplasticNetwork(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ARRUDA_BOYCE_PLASTIC",
        description="Schema name: ArrudaBoycePlasticElastoplasticNetwork",
    )
    nk_theta_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="nkThetaFunction", serialization_alias="nkThetaFunction", default=None
    )
    chain_length_function: OneOf_ArrudaBoycePlasticElastoplasticNetworkChainLengthFunction | None = Field(
        validation_alias="chainLengthFunction", serialization_alias="chainLengthFunction", default=None
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
