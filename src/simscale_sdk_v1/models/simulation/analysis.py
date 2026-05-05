from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.compressible import Compressible
from simscale_sdk_v1.models.simulation.conjugate_heat_transfer import ConjugateHeatTransfer
from simscale_sdk_v1.models.simulation.convective_heat_transfer import ConvectiveHeatTransfer
from simscale_sdk_v1.models.simulation.coupled_conjugate_heat_transfer import CoupledConjugateHeatTransfer
from simscale_sdk_v1.models.simulation.dynamic_analysis import DynamicAnalysis
from simscale_sdk_v1.models.simulation.electromagnetic_analysis import ElectromagneticAnalysis
from simscale_sdk_v1.models.simulation.embedded_boundary import EmbeddedBoundary
from simscale_sdk_v1.models.simulation.frequency_analysis import FrequencyAnalysis
from simscale_sdk_v1.models.simulation.harmonic_analysis import HarmonicAnalysis
from simscale_sdk_v1.models.simulation.heat_transfer import HeatTransfer
from simscale_sdk_v1.models.simulation.incompressible import Incompressible
from simscale_sdk_v1.models.simulation.incompressible_pacefish import IncompressiblePacefish
from simscale_sdk_v1.models.simulation.marc_analysis import MarcAnalysis
from simscale_sdk_v1.models.simulation.multiphase import Multiphase
from simscale_sdk_v1.models.simulation.simerics_analysis import SimericsAnalysis
from simscale_sdk_v1.models.simulation.static_analysis import StaticAnalysis
from simscale_sdk_v1.models.simulation.thermal_mechanical import ThermalMechanical
from simscale_sdk_v1.models.simulation.wind_comfort import WindComfort

_ANALYSIS_VARIANTS: dict[str, type] = {
    "STATIC_ANALYSIS": StaticAnalysis,
    "DYNAMIC_ANALYSIS": DynamicAnalysis,
    "HEAT_TRANSFER": HeatTransfer,
    "THERMAL_MECHANICAL": ThermalMechanical,
    "INCOMPRESSIBLE": Incompressible,
    "INCOMPRESSIBLE_PACEFISH": IncompressiblePacefish,
    "SIMERICS_ANALYSIS": SimericsAnalysis,
    "WIND_COMFORT": WindComfort,
    "COMPRESSIBLE": Compressible,
    "CONVECTIVE_HEAT_TRANSFER": ConvectiveHeatTransfer,
    "COUPLED_CONJUGATE_HEAT_TRANSFER": CoupledConjugateHeatTransfer,
    "EMBEDDED_BOUNDARY": EmbeddedBoundary,
    "MULTIPHASE": Multiphase,
    "CONJUGATE_HEAT_TRANSFER": ConjugateHeatTransfer,
    "HARMONIC_ANALYSIS": HarmonicAnalysis,
    "FREQUENCY_ANALYSIS": FrequencyAnalysis,
    "ELECTROMAGNETIC_ANALYSIS": ElectromagneticAnalysis,
    "MARC_ANALYSIS": MarcAnalysis,
}

Analysis = Annotated[
    Union[
        StaticAnalysis,
        DynamicAnalysis,
        HeatTransfer,
        ThermalMechanical,
        Incompressible,
        IncompressiblePacefish,
        SimericsAnalysis,
        WindComfort,
        Compressible,
        ConvectiveHeatTransfer,
        CoupledConjugateHeatTransfer,
        EmbeddedBoundary,
        Multiphase,
        ConjugateHeatTransfer,
        HarmonicAnalysis,
        FrequencyAnalysis,
        ElectromagneticAnalysis,
        MarcAnalysis,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ANALYSIS_VARIANTS,
        )
    ),
]
