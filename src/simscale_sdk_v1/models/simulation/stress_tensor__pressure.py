from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xx import (
    OneOf_StressTensor_PressureSigmaXX,
)
from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xy import (
    OneOf_StressTensor_PressureSigmaXY,
)
from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xz import (
    OneOf_StressTensor_PressureSigmaXZ,
)
from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_yy import (
    OneOf_StressTensor_PressureSigmaYY,
)
from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_yz import (
    OneOf_StressTensor_PressureSigmaYZ,
)
from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_zz import (
    OneOf_StressTensor_PressureSigmaZZ,
)


class StressTensor_Pressure(SimScaleModel):
    sigma_xx: OneOf_StressTensor_PressureSigmaXX | None = Field(
        validation_alias="sigmaXX", serialization_alias="sigmaXX", default=None
    )
    sigma_yy: OneOf_StressTensor_PressureSigmaYY | None = Field(
        validation_alias="sigmaYY", serialization_alias="sigmaYY", default=None
    )
    sigma_zz: OneOf_StressTensor_PressureSigmaZZ | None = Field(
        validation_alias="sigmaZZ", serialization_alias="sigmaZZ", default=None
    )
    sigma_yz: OneOf_StressTensor_PressureSigmaYZ | None = Field(
        validation_alias="sigmaYZ", serialization_alias="sigmaYZ", default=None
    )
    sigma_xz: OneOf_StressTensor_PressureSigmaXZ | None = Field(
        validation_alias="sigmaXZ", serialization_alias="sigmaXZ", default=None
    )
    sigma_xy: OneOf_StressTensor_PressureSigmaXY | None = Field(
        validation_alias="sigmaXY", serialization_alias="sigmaXY", default=None
    )
    unit: Literal[
        "Pa",
        "lbf/in²",
        "hPa",
        "kPa",
        "MPa",
        "atm",
        "mbar",
        "bar",
        "mH2O",
        "mmH2O",
        "mmHg",
        "dyne/cm²",
        "inH2O",
        "ftH2O",
        "inHg",
        "psf",
    ]
