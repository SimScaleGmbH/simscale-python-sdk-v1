from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_contact_friction_stress_type import MarcContactFrictionStressType
from simscale_sdk_v1.models.simulation.marc_contact_gap_type import MarcContactGapType
from simscale_sdk_v1.models.simulation.marc_contact_normal_stress_type import MarcContactNormalStressType
from simscale_sdk_v1.models.simulation.marc_contact_pressure_type import MarcContactPressureType
from simscale_sdk_v1.models.simulation.marc_contact_status_type import MarcContactStatusType

# Normal stress: The contact pressure distributed over the interface area, acting perpendicular to the surfaces.Friction stress: The shear stress distributed over the contact interface resulting from friction.Gap: The physical distance between two potential contact surfaces; a value of zero (or a very small tolerance) indicates the surfaces are in contact.State: A status indicator showing whether a contact pair is open (no contact), closed (sticking), or sliding.Pressure: The magnitude of the normal compressive stress exerted by one body onto another at the contact interface.
_ONE_OF__MARC_CONTACT_FIELD_SELECTION_CONTACT_TYPE_VARIANTS: dict[str, type] = {
    "NORMAL_STRESS": MarcContactNormalStressType,
    "FRICTION_STRESS": MarcContactFrictionStressType,
    "GAP": MarcContactGapType,
    "STATUS": MarcContactStatusType,
    "PRESSURE": MarcContactPressureType,
}

OneOf_MarcContactFieldSelectionContactType = Annotated[
    Union[
        MarcContactNormalStressType,
        MarcContactFrictionStressType,
        MarcContactGapType,
        MarcContactStatusType,
        MarcContactPressureType,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_CONTACT_FIELD_SELECTION_CONTACT_TYPE_VARIANTS,
        )
    ),
]
