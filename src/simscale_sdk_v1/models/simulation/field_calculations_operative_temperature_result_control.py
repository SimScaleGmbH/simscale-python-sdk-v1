from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.mrt_solar_parameters import MrtSolarParameters
from simscale_sdk_v1.models.simulation.operative_temperature_result_type import OperativeTemperatureResultType


class FieldCalculationsOperativeTemperatureResultControl(SimScaleModel):
    """Computes the Operative Temperature. It is defined as the uniform surface temperature of an imaginary black enclosure in which an every point of the domain would exchange the same amount of convective and radiative heat as in the actual nonuniform space"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OPERATIVE_TEMPERATURE",
        description="Computes the Operative Temperature. It is defined as the uniform surface temperature of an imaginary black enclosure in which an every point of the domain would exchange the same amount of convective and radiative heat as in the actual nonuniform space  Schema name: FieldCalculationsOperativeTemperatureResultControl",
    )
    name: str | None = Field(default=None)
    result_type: OperativeTemperatureResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
    mrt_solar_parameters: MrtSolarParameters | None = Field(
        validation_alias="mrtSolarParameters", serialization_alias="mrtSolarParameters", default=None
    )
