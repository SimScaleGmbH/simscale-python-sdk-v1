from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.false_change_jacobian_matrix import FalseChangeJacobianMatrix
from simscale_sdk_v1.models.simulation.true_change_jacobian_matrix import TrueChangeJacobianMatrix

# Choose if the Jacobian matrix should automatically change from tangent stiffnes matrix to elastic matrix if the time increment is falling below a given threshold. On the assumption that below a given time increment value the nonlinearities are not evolving within the time step one can strongly save computation time by switching to the elastic matrix.
_ONE_OF__TANGENT_JACOBIAN_MATRIX_CHANGE_JACOBIAN_MATRIX_VARIANTS: dict[str, type] = {
    "TRUE": TrueChangeJacobianMatrix,
    "FALSE": FalseChangeJacobianMatrix,
}

OneOf_TangentJacobianMatrixChangeJacobianMatrix = Annotated[
    Union[TrueChangeJacobianMatrix, FalseChangeJacobianMatrix],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__TANGENT_JACOBIAN_MATRIX_CHANGE_JACOBIAN_MATRIX_VARIANTS,
        )
    ),
]
