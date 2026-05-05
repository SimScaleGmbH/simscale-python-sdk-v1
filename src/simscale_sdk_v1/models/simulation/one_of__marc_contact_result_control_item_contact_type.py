from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_contact_friction_force import MarcContactFrictionForce
from simscale_sdk_v1.models.simulation.marc_contact_friction_stress import MarcContactFrictionStress
from simscale_sdk_v1.models.simulation.marc_contact_gap import MarcContactGap
from simscale_sdk_v1.models.simulation.marc_contact_normal_force import MarcContactNormalForce
from simscale_sdk_v1.models.simulation.marc_contact_normal_stress import MarcContactNormalStress
from simscale_sdk_v1.models.simulation.marc_contact_pressure import MarcContactPressure
from simscale_sdk_v1.models.simulation.marc_contact_status import MarcContactStatus

# Normal force: The compressive force acting perpendicular to the contact interface between two bodies.Friction force: The tangential shear force generated at a contact interface that resists relative sliding between two bodies due to friction.Normal stress: The contact pressure distributed over the interface area, acting perpendicular to the surfaces.Friction stress: The shear stress distributed over the contact interface resulting from friction.Gap: The physical distance between two potential contact surfaces; a value of zero (or a very small tolerance) indicates the surfaces are in contact.State: A status indicator showing whether a contact pair is open (no contact), closed (sticking), or sliding.Pressure: The magnitude of the normal compressive stress exerted by one body onto another at the contact interface.
_ONE_OF__MARC_CONTACT_RESULT_CONTROL_ITEM_CONTACT_TYPE_VARIANTS: dict[str, type] = {
    "NORMAL_FORCE": MarcContactNormalForce,
    "FRICTION_FORCE": MarcContactFrictionForce,
    "NORMAL_STRESS": MarcContactNormalStress,
    "FRICTION_STRESS": MarcContactFrictionStress,
    "GAP": MarcContactGap,
    "STATUS": MarcContactStatus,
    "PRESSURE": MarcContactPressure,
}

OneOf_MarcContactResultControlItemContactType = Annotated[
    Union[
        MarcContactNormalForce,
        MarcContactFrictionForce,
        MarcContactNormalStress,
        MarcContactFrictionStress,
        MarcContactGap,
        MarcContactStatus,
        MarcContactPressure,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_CONTACT_RESULT_CONTROL_ITEM_CONTACT_TYPE_VARIANTS,
        )
    ),
]
