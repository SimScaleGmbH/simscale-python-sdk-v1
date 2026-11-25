from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.mass_from_density import MassFromDensity
from simscale_sdk_v1.models.simulation.specified_mass import SpecifiedMass

# How the mass of the moving body is obtained.Specified &mdash; enter the mass directly. The usual choice, since a data sheet normally quotes it.From density &mdash; the mass is computed as the density of the material assigned to the body times the volume of its mesh. The electromagnetic material needs a density for this.
_ONE_OF__COMPUTED_TRANSLATIONAL_MOTION_MASS_DEFINITION_VARIANTS: dict[str, type] = {
    "SPECIFIED_MASS": SpecifiedMass,
    "MASS_FROM_DENSITY": MassFromDensity,
}

OneOf_ComputedTranslationalMotionMassDefinition = Annotated[
    Union[SpecifiedMass, MassFromDensity],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__COMPUTED_TRANSLATIONAL_MOTION_MASS_DEFINITION_VARIANTS,
        )
    ),
]
