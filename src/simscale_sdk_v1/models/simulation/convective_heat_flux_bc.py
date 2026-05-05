from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_transmittance import (
    DimensionalFunction_ThermalTransmittance,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ConvectiveHeatFluxBC(SimScaleModel):
    """This is a heat flux boundary condition representing a convective heat flux on the selected face groups. It is defined by the reference temperature (surrounding temperature) and the convection coefficient.Important remarks: The convection coefficient is not only dependent on the material of the surrounding fluid but a property of the flowYou may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file) for the reference temperature and the convection coefficient"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONVECTIVE_HEAT_FLUX",
        description="This is a heat flux boundary condition representing a convective heat flux on the selected face groups. It is defined by the reference temperature (surrounding temperature) and the convection coefficient.Important remarks: The convection coefficient is not only dependent on the material of the surrounding fluid but a property of the flowYou may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file) for the reference temperature and the convection coefficient  Schema name: ConvectiveHeatFluxBC",
    )
    name: str | None = Field(default=None)
    reference_temperature: DimensionalFunction_Temperature | None = Field(
        validation_alias="referenceTemperature", serialization_alias="referenceTemperature", default=None
    )
    heat_transfer_coefficient: DimensionalFunction_ThermalTransmittance | None = Field(
        validation_alias="heatTransferCoefficient", serialization_alias="heatTransferCoefficient", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
