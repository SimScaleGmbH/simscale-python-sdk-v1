from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AiUserModel(SimScaleModel):
    analysis_type: str | None = Field(
        validation_alias="analysisType",
        serialization_alias="analysisType",
        default=None,
        description="Possible values are STATIC_ANALYSIS, INCOMPRESSIBLE, COUPLED_CONJUGATE_HEAT_TRANSFER and EMBEDDED_BOUNDARY",
    )
    name: str | None = Field(default=None)
    predictor_component: str | None = Field(
        validation_alias="predictorComponent",
        serialization_alias="predictorComponent",
        default=None,
        description="Possible values are navasto and ai-solver-kickstart",
    )
    shared_with_organization: bool | None = Field(
        validation_alias="sharedWithOrganization", serialization_alias="sharedWithOrganization", default=None
    )
    template_name: str | None = Field(
        validation_alias="templateName",
        serialization_alias="templateName",
        default=None,
        description="Possible values are fea_template, cfd_template, chtv2ibm_template, spec_id and spec_and_tesselation",
    )
    template_parameters: dict[str, Any] | None = Field(
        validation_alias="templateParameters", serialization_alias="templateParameters", default=None
    )
    ai_model_id: str | None = Field(validation_alias="aiModelId", serialization_alias="aiModelId", default=None)
