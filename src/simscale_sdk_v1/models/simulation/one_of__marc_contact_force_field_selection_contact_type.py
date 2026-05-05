from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_contact_body_force_type import MarcContactBodyForceType
from simscale_sdk_v1.models.simulation.marc_contact_friction_force_type import MarcContactFrictionForceType
from simscale_sdk_v1.models.simulation.marc_contact_normal_force_type import MarcContactNormalForceType

# Normal force: The compressive force acting perpendicular to the contact interface between two bodies.Friction force: The tangential shear force generated at a contact interface that resists relative sliding between two bodies due to friction.Contact body force: Computes the total resultant force vector acting on a specific body due to all its active contact interactions. Available in volume sum only.
_ONE_OF__MARC_CONTACT_FORCE_FIELD_SELECTION_CONTACT_TYPE_VARIANTS: dict[str, type] = {
    "NORMAL_FORCE": MarcContactNormalForceType,
    "FRICTION_FORCE": MarcContactFrictionForceType,
    "BODY_FORCE": MarcContactBodyForceType,
}

OneOf_MarcContactForceFieldSelectionContactType = Annotated[
    Union[MarcContactNormalForceType, MarcContactFrictionForceType, MarcContactBodyForceType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_CONTACT_FORCE_FIELD_SELECTION_CONTACT_TYPE_VARIANTS,
        )
    ),
]
