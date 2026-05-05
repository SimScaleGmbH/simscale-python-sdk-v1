from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_humidity_sources import (
    OneOf_AdvancedConceptsHumiditySources,
)
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_momentum_sources import (
    OneOf_AdvancedConceptsMomentumSources,
)
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_passive_scalar_sources import (
    OneOf_AdvancedConceptsPassiveScalarSources,
)
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_porous_mediums import (
    OneOf_AdvancedConceptsPorousMediums,
)
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_power_sources import OneOf_AdvancedConceptsPowerSources
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_rotating_zones import (
    OneOf_AdvancedConceptsRotatingZones,
)
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_solid_body_motions import (
    OneOf_AdvancedConceptsSolidBodyMotions,
)
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_thermal_contact_resistance import (
    OneOf_AdvancedConceptsThermalContactResistance,
)
from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_thermal_resistance_networks import (
    OneOf_AdvancedConceptsThermalResistanceNetworks,
)


class AdvancedConcepts(SimScaleModel):
    thermal_contact_resistance: list[OneOf_AdvancedConceptsThermalContactResistance] | None = Field(
        validation_alias="thermalContactResistance", serialization_alias="thermalContactResistance", default=None
    )
    humidity_sources: list[OneOf_AdvancedConceptsHumiditySources] | None = Field(
        validation_alias="humiditySources", serialization_alias="humiditySources", default=None
    )
    momentum_sources: list[OneOf_AdvancedConceptsMomentumSources] | None = Field(
        validation_alias="momentumSources", serialization_alias="momentumSources", default=None
    )
    passive_scalar_sources: list[OneOf_AdvancedConceptsPassiveScalarSources] | None = Field(
        validation_alias="passiveScalarSources", serialization_alias="passiveScalarSources", default=None
    )
    porous_mediums: list[OneOf_AdvancedConceptsPorousMediums] | None = Field(
        validation_alias="porousMediums", serialization_alias="porousMediums", default=None
    )
    power_sources: list[OneOf_AdvancedConceptsPowerSources] | None = Field(
        validation_alias="powerSources", serialization_alias="powerSources", default=None
    )
    rotating_zones: list[OneOf_AdvancedConceptsRotatingZones] | None = Field(
        validation_alias="rotatingZones", serialization_alias="rotatingZones", default=None
    )
    solid_body_motions: list[OneOf_AdvancedConceptsSolidBodyMotions] | None = Field(
        validation_alias="solidBodyMotions", serialization_alias="solidBodyMotions", default=None
    )
    thermal_resistance_networks: list[OneOf_AdvancedConceptsThermalResistanceNetworks] | None = Field(
        validation_alias="thermalResistanceNetworks", serialization_alias="thermalResistanceNetworks", default=None
    )
