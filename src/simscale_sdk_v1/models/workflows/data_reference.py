from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DataReference(SimScaleModel):
    """Reference to a data in a workflow.  It is used to wire together the workflow topology and also used in the algorithms for the workflow execution.  Specific subtypes are generated for each data type for type safe wiring."""

    data_name: str | None = Field(validation_alias="dataName", serialization_alias="dataName", default=None)
    data_type_reference: str | None = Field(
        validation_alias="dataTypeReference", serialization_alias="dataTypeReference", default=None
    )
    doc: str | None = Field(default=None)
    label: str | None = Field(default=None)
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
    multi_language_label: dict[str, str] | None = Field(
        validation_alias="multiLanguageLabel", serialization_alias="multiLanguageLabel", default=None
    )
