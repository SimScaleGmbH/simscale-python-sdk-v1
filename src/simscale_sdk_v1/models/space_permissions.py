from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SpacePermissions(SimScaleModel):
    """Permissions that the current user has on this Space. Each flag corresponds to a fine-grained action that a user may take."""

    can_list_content_in_root: bool | None = Field(
        validation_alias="canListContentInRoot",
        serialization_alias="canListContentInRoot",
        default=None,
        description="Whether the current user can list the contents of the root of this Space.",
    )
    can_create_content_in_root: bool | None = Field(
        validation_alias="canCreateContentInRoot",
        serialization_alias="canCreateContentInRoot",
        default=None,
        description="Whether the current user can create new content in the root of this Space.",
    )
    can_move_content_to_root: bool | None = Field(
        validation_alias="canMoveContentToRoot",
        serialization_alias="canMoveContentToRoot",
        default=None,
        description="Whether the current user can move content into the root folder of this Space.",
    )
    can_move_content_out_of_root: bool | None = Field(
        validation_alias="canMoveContentOutOfRoot",
        serialization_alias="canMoveContentOutOfRoot",
        default=None,
        description="Whether the current user can move content out of the root folder of this Space.",
    )
    can_edit_space_metadata: bool | None = Field(
        validation_alias="canEditSpaceMetadata",
        serialization_alias="canEditSpaceMetadata",
        default=None,
        description="Whether the current user can edit the metadata of this Space.",
    )
    can_edit_space_settings: bool | None = Field(
        validation_alias="canEditSpaceSettings",
        serialization_alias="canEditSpaceSettings",
        default=None,
        description="Whether the current user can edit the settings of this Space.",
    )
    can_edit_space_permissions: bool | None = Field(
        validation_alias="canEditSpacePermissions",
        serialization_alias="canEditSpacePermissions",
        default=None,
        description="Whether the current user can add or remove users to this Space.",
    )
    can_delete_space: bool | None = Field(
        validation_alias="canDeleteSpace",
        serialization_alias="canDeleteSpace",
        default=None,
        description="Whether the current user can delete this Space.",
    )
