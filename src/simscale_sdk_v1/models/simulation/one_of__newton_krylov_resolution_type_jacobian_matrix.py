from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.elastic_jacobian_matrix import ElasticJacobianMatrix
from simscale_sdk_v1.models.simulation.tangent_jacobian_matrix import TangentJacobianMatrix

_ONE_OF__NEWTON_KRYLOV_RESOLUTION_TYPE_JACOBIAN_MATRIX_VARIANTS: dict[str, type] = {
    "TANGENT": TangentJacobianMatrix,
    "ELASTIC": ElasticJacobianMatrix,
}

OneOf_NewtonKrylovResolutionTypeJacobianMatrix = Annotated[
    Union[TangentJacobianMatrix, ElasticJacobianMatrix],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__NEWTON_KRYLOV_RESOLUTION_TYPE_JACOBIAN_MATRIX_VARIANTS,
        )
    ),
]
