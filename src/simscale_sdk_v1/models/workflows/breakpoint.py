from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Breakpoint(SimScaleModel):
    """Breakpoints provide an automated mechanism to pause a workflow run based on certain criteria.  Based on the criteria the following cases are possible: * operation only breakpoint: the workflow gets automatically paused when the workflow run would get to the processing of a particular operation * condition only breakpoint: the workflow gets automatically paused when the particular condition (expressed as a boolean value model) becomes true * operation with condition breakpoint: the workflow gets automatically paused when the workflow run gets to the processing of a particular operation and also the additional condition is met  In all cases, whenever a breakpoints get activated, the workflow executor puts the workflow run into paused state and not scheduling any further operation processing until the workflow run is resumed explicitly by the user. That's also true for those operations which has no associated activated breakpoint, in other words, there's no concept of "multi-threading" in workflows in the sense of pausing one "thread" and keeping others running, even if when the run is ongoing maximum parallelism is aimed by the workflow executor. Note that already running operations are allowed to finish and to be processed in case of breakpoint activation, but after their processing the workflow run is completely paused and not reprocessed for other potential further operations.  Breakpoints can be defined at these levels: * workflow type level: defined as part of the workflow definition by the workflow developer, these breakpoints apply to all workflows and their runs based on top of the particular workflow type * workflow level: users can define workflow specific custom breakpoints which apply only to the particular workflow and its runs * workflow run level: users can also define workflow run specific custom breakpoints which apply only to the particular workflow run"""

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
