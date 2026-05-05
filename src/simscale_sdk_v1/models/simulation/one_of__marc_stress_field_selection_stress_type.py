from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_cauchy_stress_type import MarcCauchyStressType
from simscale_sdk_v1.models.simulation.marc_principal_stress_type import MarcPrincipalStressType
from simscale_sdk_v1.models.simulation.marc_von_mises_stress_type import MarcVonMisesStressType

# Cauchy stress: Also known as "true stress," it represents the force per unit of current (deformed) area. This is the standard stress measure for large deformation nonlinear analysis. Tensor quantity.Von Mises stress: A scalar value used to predict yielding of ductile materials; it represents the "distortional energy" within the body.Principal stress: The normal stresses acting on planes where the shear stresses are zero (&sigma;1, &sigma;2, &sigma;3), indicating the extreme tension or compression values.
_ONE_OF__MARC_STRESS_FIELD_SELECTION_STRESS_TYPE_VARIANTS: dict[str, type] = {
    "CAUCHY": MarcCauchyStressType,
    "VON_MISES": MarcVonMisesStressType,
    "PRINCIPAL": MarcPrincipalStressType,
}

OneOf_MarcStressFieldSelectionStressType = Annotated[
    Union[MarcCauchyStressType, MarcVonMisesStressType, MarcPrincipalStressType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_STRESS_FIELD_SELECTION_STRESS_TYPE_VARIANTS,
        )
    ),
]
