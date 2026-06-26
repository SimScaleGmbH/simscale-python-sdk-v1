"""Generated DataRepository models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.data_repository.create_upload_session_request import CreateUploadSessionRequest
    from simscale_sdk_v1.models.data_repository.data_info import DataInfo
    from simscale_sdk_v1.models.data_repository.external_data_info import ExternalDataInfo
    from simscale_sdk_v1.models.data_repository.http_header import HttpHeader
    from simscale_sdk_v1.models.data_repository.internal_data_info import InternalDataInfo
    from simscale_sdk_v1.models.data_repository.presigned_request import PresignedRequest
    from simscale_sdk_v1.models.data_repository.start_upload_session_append_request import (
        StartUploadSessionAppendRequest,
    )
    from simscale_sdk_v1.models.data_repository.upload_session import UploadSession
    from simscale_sdk_v1.models.data_repository.upload_session_append import UploadSessionAppend

_NAMES: dict[str, tuple[str, str]] = {
    "CreateUploadSessionRequest": (
        "simscale_sdk_v1.models.data_repository.create_upload_session_request",
        "CreateUploadSessionRequest",
    ),
    "DataInfo": ("simscale_sdk_v1.models.data_repository.data_info", "DataInfo"),
    "ExternalDataInfo": ("simscale_sdk_v1.models.data_repository.external_data_info", "ExternalDataInfo"),
    "HttpHeader": ("simscale_sdk_v1.models.data_repository.http_header", "HttpHeader"),
    "InternalDataInfo": ("simscale_sdk_v1.models.data_repository.internal_data_info", "InternalDataInfo"),
    "PresignedRequest": ("simscale_sdk_v1.models.data_repository.presigned_request", "PresignedRequest"),
    "StartUploadSessionAppendRequest": (
        "simscale_sdk_v1.models.data_repository.start_upload_session_append_request",
        "StartUploadSessionAppendRequest",
    ),
    "UploadSession": ("simscale_sdk_v1.models.data_repository.upload_session", "UploadSession"),
    "UploadSessionAppend": ("simscale_sdk_v1.models.data_repository.upload_session_append", "UploadSessionAppend"),
}


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys())
