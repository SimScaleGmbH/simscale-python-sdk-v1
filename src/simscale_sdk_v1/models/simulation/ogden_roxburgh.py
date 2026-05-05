from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__energy_density import Dimensional_EnergyDensity


class OgdenRoxburgh(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OGDEN_ROXBURGH",
        description="Schema name: OgdenRoxburgh",
    )
    relative_damage_extent: float | None = Field(
        validation_alias="relativeDamageExtent",
        serialization_alias="relativeDamageExtent",
        default=None,
        description="This parameter (r ≥ 1) dictates the maximum magnitude of damage achievable in the Ogden-Roxburgh model. Higher values lead to a more pronounced reduction in material stiffness during unloading and reloading cycles, characteristic of the Mullins effect.",
    )
    deformation_dependence: Dimensional_EnergyDensity | None = Field(
        validation_alias="deformationDependence", serialization_alias="deformationDependence", default=None
    )
    deviatoric_strain_energy_factor: float | None = Field(
        validation_alias="deviatoricStrainEnergyFactor",
        serialization_alias="deviatoricStrainEnergyFactor",
        default=None,
        description="A scaling factor (β ≥ 0) that adjusts the influence of the shape-changing (deviatoric) part of the strain energy on the damage evolution. It allows the model to prioritize distortion over volume change when calculating the softening effect.",
    )
