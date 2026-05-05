from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_density import (
    OneOf_SpatialDiscretizationSchemesDensity,
)
from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_gas_mixture_transport import (
    OneOf_SpatialDiscretizationSchemesGasMixtureTransport,
)
from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_internal_energy import (
    OneOf_SpatialDiscretizationSchemesInternalEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_turbulent_energy_dissipation_rate import (
    OneOf_SpatialDiscretizationSchemesTurbulentEnergyDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_turbulent_kinetic_energy import (
    OneOf_SpatialDiscretizationSchemesTurbulentKineticEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_velocity import (
    OneOf_SpatialDiscretizationSchemesVelocity,
)
from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_volume_of_fluid import (
    OneOf_SpatialDiscretizationSchemesVolumeOfFluid,
)


class SpatialDiscretizationSchemes(SimScaleModel):
    velocity: OneOf_SpatialDiscretizationSchemesVelocity | None = Field(default=None)
    density: OneOf_SpatialDiscretizationSchemesDensity | None = Field(default=None)
    turbulent_kinetic_energy: OneOf_SpatialDiscretizationSchemesTurbulentKineticEnergy | None = Field(
        validation_alias="turbulentKineticEnergy", serialization_alias="turbulentKineticEnergy", default=None
    )
    turbulent_energy_dissipation_rate: OneOf_SpatialDiscretizationSchemesTurbulentEnergyDissipationRate | None = Field(
        validation_alias="turbulentEnergyDissipationRate",
        serialization_alias="turbulentEnergyDissipationRate",
        default=None,
    )
    volume_of_fluid: OneOf_SpatialDiscretizationSchemesVolumeOfFluid | None = Field(
        validation_alias="volumeOfFluid", serialization_alias="volumeOfFluid", default=None
    )
    internal_energy: OneOf_SpatialDiscretizationSchemesInternalEnergy | None = Field(
        validation_alias="internalEnergy", serialization_alias="internalEnergy", default=None
    )
    gas_mixture_transport: OneOf_SpatialDiscretizationSchemesGasMixtureTransport | None = Field(
        validation_alias="gasMixtureTransport", serialization_alias="gasMixtureTransport", default=None
    )
