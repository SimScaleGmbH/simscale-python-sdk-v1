from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_transmittance import (
    DimensionalFunction_ThermalTransmittance,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ConvectionRadiationBCMarc(SimScaleModel):
    """This is a heat flux boundary condition combining convection and radiation on the selected face groups. It is defined by a common reference temperature (surrounding/sink temperature), the heat transfer coefficient (convective part) and the emissivity (radiative part).Important remarks: The heat transfer coefficient is not only a property of the surrounding fluid but also of the flow.The emissivity takes values between 0 and 1: a value of 1 represents blackbody radiation, while the default value of 0 disables the radiative contribution, leaving a pure convection boundary condition.Radiation is considered diffuse and gray (no dependency on the rotational angle or wavelength).If the reference temperature is higher than the computed temperature on the boundary, heat flux enters the body; for lower values, heat flux leaves the body.You may define a time dependent value by defining a formula or uploading a table (csv-file) for the reference temperature, the heat transfer coefficient and the emissivity."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONVECTION_RADIATION",
        description="This is a heat flux boundary condition combining convection and radiation on the selected face groups. It is defined by a common reference temperature (surrounding/sink temperature), the heat transfer coefficient (convective part) and the emissivity (radiative part).Important remarks: The heat transfer coefficient is not only a property of the surrounding fluid but also of the flow.The emissivity takes values between 0 and 1: a value of 1 represents blackbody radiation, while the default value of 0 disables the radiative contribution, leaving a pure convection boundary condition.Radiation is considered diffuse and gray (no dependency on the rotational angle or wavelength).If the reference temperature is higher than the computed temperature on the boundary, heat flux enters the body; for lower values, heat flux leaves the body.You may define a time dependent value by defining a formula or uploading a table (csv-file) for the reference temperature, the heat transfer coefficient and the emissivity.  Schema name: ConvectionRadiationBCMarc",
    )
    name: str | None = Field(default=None)
    reference_temperature: DimensionalFunction_Temperature | None = Field(
        validation_alias="referenceTemperature", serialization_alias="referenceTemperature", default=None
    )
    heat_transfer_coefficient: DimensionalFunction_ThermalTransmittance | None = Field(
        validation_alias="heatTransferCoefficient", serialization_alias="heatTransferCoefficient", default=None
    )
    emissivity: DimensionalFunction_Dimensionless | None = Field(default=None)
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
