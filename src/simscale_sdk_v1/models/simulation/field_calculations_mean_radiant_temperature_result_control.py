from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.mean_radiant_temperature_result_type import MeanRadiantTemperatureResultType
from simscale_sdk_v1.models.simulation.mrt_solar_parameters import MrtSolarParameters


class FieldCalculationsMeanRadiantTemperatureResultControl(SimScaleModel):
    """Computes the Mean Radiant Temperature (MRT). It is defined as the uniform surface temperature of an imaginary black enclosure in which an every point of the domain would exchange the same amount of radiative heat as in the actual nonuniform space"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MEAN_RADIANT_TEMPERATURE",
        description="Computes the Mean Radiant Temperature (MRT). It is defined as the uniform surface temperature of an imaginary black enclosure in which an every point of the domain would exchange the same amount of radiative heat as in the actual nonuniform space  Schema name: FieldCalculationsMeanRadiantTemperatureResultControl",
    )
    name: str | None = Field(default=None)
    result_type: MeanRadiantTemperatureResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
    mrt_solar_parameters: MrtSolarParameters | None = Field(
        validation_alias="mrtSolarParameters", serialization_alias="mrtSolarParameters", default=None
    )
