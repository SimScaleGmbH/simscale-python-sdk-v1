from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ErrorResponse(SimScaleModel):
    error_code: str | None = Field(validation_alias="errorCode", serialization_alias="errorCode", default=None)
    error_details: Any | None = Field(validation_alias="errorDetails", serialization_alias="errorDetails", default=None)
    iso_timestamp: str | None = Field(validation_alias="isoTimestamp", serialization_alias="isoTimestamp", default=None)
    message: str | None = Field(default=None)
    span_id: str | None = Field(validation_alias="spanId", serialization_alias="spanId", default=None)
    status: int | None = Field(default=None)
    timestamp: int | None = Field(default=None)
    trace_id: str | None = Field(validation_alias="traceId", serialization_alias="traceId", default=None)
