from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.electrostatics import Electrostatics
from simscale_sdk_v1.models.simulation.magnetostatics import Magnetostatics
from simscale_sdk_v1.models.simulation.time_harmonic_electrics import TimeHarmonicElectrics
from simscale_sdk_v1.models.simulation.time_harmonic_magnetics import TimeHarmonicMagnetics
from simscale_sdk_v1.models.simulation.time_transient_magnetics import TimeTransientMagnetics

# ElectrostaticsUse for problems where electric fields and charges are stationary, and no time-varying electromagnetic fields are present.MagnetostaticsUse for problems where magnetic fields are constant over time and thus no eddy currents are present. Time-Harmonic MagneticsUse for problems where magnetic fields and electric currents are sinusoidally varying. Time-Transient MagneticsUse for problems where magnetic fields and electric currents are time-dependent.Learn more
_ONE_OF__ELECTROMAGNETIC_ANALYSIS_MODEL_VARIANTS: dict[str, type] = {
    "ELECTROSTATICS": Electrostatics,
    "TIME_HARMONIC_ELECTRICS": TimeHarmonicElectrics,
    "MAGNETOSTATICS": Magnetostatics,
    "TIME_HARMONIC_MAGNETICS": TimeHarmonicMagnetics,
    "TIME_TRANSIENT_MAGNETICS": TimeTransientMagnetics,
}

OneOf_ElectromagneticAnalysisModel = Annotated[
    Union[Electrostatics, TimeHarmonicElectrics, Magnetostatics, TimeHarmonicMagnetics, TimeTransientMagnetics],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_ANALYSIS_MODEL_VARIANTS,
        )
    ),
]
