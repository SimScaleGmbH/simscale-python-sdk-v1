from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Breakpoint(SimScaleModel):
    """Breakpoints provide an automated mechanism to pause a workflow run based on certain criteria.  Based on the criteria the following cases are possible: * operation only breakpoint: the workflow gets automatically paused when the workflow run would get to the processing of a particular operation * condition only breakpoint: the workflow gets automatically paused when the particular condition (expressed as a boolean value model) becomes true * operation with condition breakpoint: the workflow gets automatically paused when the workflow run gets to the processing of a particular operation and also the additional condition is met  An operation breakpoint is evaluated after the workflow graph identifies the referenced operation as executable, but before that operation is scheduled. Results required from preceding operations have therefore already been incorporated into the workflow and are available for inspection while paused; the referenced operation has not started yet.  When a breakpoint is activated, the workflow run enters the paused state until the user explicitly resumes it. The pause applies to the whole workflow, including operations without the activated breakpoint; workflows do not have independently progressing "threads", and no further operations are scheduled while the workflow remains paused.  Activating a breakpoint does not cancel operations that are already running. They may finish while the workflow is paused, but results that complete after the pause remain waiting without being incorporated into the workflow and are processed only after resume.  Breakpoints can be defined at these levels: * workflow type level: defined as part of the workflow definition by the workflow developer, these breakpoints apply to all workflows and their runs based on top of the particular workflow type * workflow level: users can define workflow specific custom breakpoints which apply only to the particular workflow and its runs * workflow run level: users can also define workflow run specific custom breakpoints which apply only to the particular workflow run"""

    condition: Any | None = Field(
        default=None, description="Value model of a boolean value. Resolves to a JSON boolean or null node."
    )
    doc: str | None = Field(default=None)
    message: str | None = Field(default=None)
    metadata: dict[str, dict[str, Any]] | None = Field(default=None)
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
    multi_language_message: dict[str, str] | None = Field(
        validation_alias="multiLanguageMessage", serialization_alias="multiLanguageMessage", default=None
    )
    name: str | None = Field(default=None)
    operation: str | None = Field(default=None)
