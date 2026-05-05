from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SwapCadRequest(SimScaleModel):
    source_cad_id: str = Field(
        validation_alias="sourceCadId", serialization_alias="sourceCadId", description="The ID of the assigned CAD."
    )
    source_cad_state_id: str = Field(
        validation_alias="sourceCadStateId",
        serialization_alias="sourceCadStateId",
        description="The ID of the assigned CAD state.",
    )
    target_cad_id: str = Field(
        validation_alias="targetCadId", serialization_alias="targetCadId", description="The ID of the CAD to assign."
    )
    target_cad_state_id: str = Field(
        validation_alias="targetCadStateId",
        serialization_alias="targetCadStateId",
        description="The ID of the CAD state to assign.",
    )
