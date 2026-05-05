from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ProjectPermissions(SimScaleModel):
    """Permissions that the current user has on this Project. Each flag corresponds to a fine-grained action that a user may take."""

    can_preview_project: bool | None = Field(
        validation_alias="canPreviewProject",
        serialization_alias="canPreviewProject",
        default=None,
        description="Whether the current user can see basic details about this Project.",
    )
    can_read_project: bool | None = Field(
        validation_alias="canReadProject",
        serialization_alias="canReadProject",
        default=None,
        description="Whether the current user can open this Project.",
    )
    can_copy_project: bool | None = Field(
        validation_alias="canCopyProject",
        serialization_alias="canCopyProject",
        default=None,
        description="Whether the current user can copy this Project.",
    )
    can_write_project: bool | None = Field(
        validation_alias="canWriteProject",
        serialization_alias="canWriteProject",
        default=None,
        description="Whether the current user can edit this Project.",
    )
    can_execute_project_billable_action: bool | None = Field(
        validation_alias="canExecuteProjectBillableAction",
        serialization_alias="canExecuteProjectBillableAction",
        default=None,
        description="Whether the current user can execute a billable action on this Project.",
    )
    can_manage_project: bool | None = Field(
        validation_alias="canManageProject",
        serialization_alias="canManageProject",
        default=None,
        description="Whether the current user can manage this Project.",
    )
    can_move_project_to_personal_space: bool | None = Field(
        validation_alias="canMoveProjectToPersonalSpace",
        serialization_alias="canMoveProjectToPersonalSpace",
        default=None,
        description="Whether the current user can move this Project to their Personal Space.",
    )
    can_list_project_permissions: bool | None = Field(
        validation_alias="canListProjectPermissions",
        serialization_alias="canListProjectPermissions",
        default=None,
        description="Whether the current user can see who has access to this Project.",
    )
    can_edit_project_permissions: bool | None = Field(
        validation_alias="canEditProjectPermissions",
        serialization_alias="canEditProjectPermissions",
        default=None,
        description="Whether the current user can change who has access to this Project.",
    )
    can_share_project_with_space_members: bool | None = Field(
        validation_alias="canShareProjectWithSpaceMembers",
        serialization_alias="canShareProjectWithSpaceMembers",
        default=None,
        description="Whether the current user can share this project with users that have access to the Space.",
    )
    can_share_project_with_organization_members: bool | None = Field(
        validation_alias="canShareProjectWithOrganizationMembers",
        serialization_alias="canShareProjectWithOrganizationMembers",
        default=None,
        description="Whether the current user can share this project with members of the Organization.",
    )
    can_share_project_with_anyone: bool | None = Field(
        validation_alias="canShareProjectWithAnyone",
        serialization_alias="canShareProjectWithAnyone",
        default=None,
        description="Whether the current user can share this project with any user of the platform.",
    )
    can_make_project_public: bool | None = Field(
        validation_alias="canMakeProjectPublic",
        serialization_alias="canMakeProjectPublic",
        default=None,
        description="Whether the current user can make this project public.",
    )
    can_delete_project: bool | None = Field(
        validation_alias="canDeleteProject",
        serialization_alias="canDeleteProject",
        default=None,
        description="Whether the current user can delete this Project.",
    )
