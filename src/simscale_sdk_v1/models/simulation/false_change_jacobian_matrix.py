from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FalseChangeJacobianMatrix(SimScaleModel):
    """Choose if the Jacobian matrix should automatically change from tangent stiffnes matrix to elastic matrix if the time increment is falling below a given threshold. On the assumption that below a given time increment value the nonlinearities are not evolving within the time step one can strongly save computation time by switching to the elastic matrix."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FALSE",
        description="Choose if the Jacobian matrix should automatically change from tangent stiffnes matrix to elastic matrix if the time increment is falling below a given threshold. On the assumption that below a given time increment value the nonlinearities are not evolving within the time step one can strongly save computation time by switching to the elastic matrix.  Schema name: FalseChangeJacobianMatrix",
    )
