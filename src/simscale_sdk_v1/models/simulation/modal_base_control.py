from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__modal_base_control_eigenfrequency_scope import (
    OneOf_ModalBaseControlEigenfrequencyScope,
)


class ModalBaseControl(SimScaleModel):
    eigenfrequency_scope: OneOf_ModalBaseControlEigenfrequencyScope | None = Field(
        validation_alias="eigenfrequencyScope", serialization_alias="eigenfrequencyScope", default=None
    )
