from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Materials:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_material(
        self,
        material_group_id: str,
        body: models.material.CreateMaterialRequest,
    ) -> models.material.MaterialResponse:
        """Create a new material"""
        return self._client.request(
            "POST",
            f"/materialgroups/{material_group_id}/materials",
            json_body=body,
            response_type=models.material.MaterialResponse,
        )

    def create_material_group(
        self,
        body: models.material.CreateMaterialGroupRequest,
    ) -> models.material.MaterialGroupResponse:
        """Create new material group"""
        return self._client.request(
            "POST",
            "/materialgroups",
            json_body=body,
            response_type=models.material.MaterialGroupResponse,
        )

    def create_nested_material_group(
        self,
        material_group_id: str,
        body: models.material.CreateNestedMaterialGroupRequest,
    ) -> models.material.MaterialGroupResponse:
        """Create a child material group for the specified parent group"""
        return self._client.request(
            "POST",
            f"/materialgroups/{material_group_id}/materialgroups",
            json_body=body,
            response_type=models.material.MaterialGroupResponse,
        )

    def delete_material_data(
        self,
        material_group_id: str,
        material_id: str,
    ) -> None:
        """Remove an existing material"""
        return self._client.request(
            "DELETE",
            f"/materialgroups/{material_group_id}/materials/{material_id}",
        )

    def delete_material_group(
        self,
        material_group_id: str,
    ) -> None:
        """Delete material group, sub-groups associated to it, and materials associated to the group and all sub-groups"""
        return self._client.request(
            "DELETE",
            f"/materialgroups/{material_group_id}",
        )

    def get_material_data(
        self,
        material_group_id: str,
        material_id: str,
    ) -> models.material.MaterialResponse:
        """Get information about an existing material"""
        return self._client.request(
            "GET",
            f"/materialgroups/{material_group_id}/materials/{material_id}",
            response_type=models.material.MaterialResponse,
        )

    def get_material_group_metadata(
        self,
        material_group_id: str,
    ) -> models.material.MaterialGroupResponse:
        """Fetch material group information"""
        return self._client.request(
            "GET",
            f"/materialgroups/{material_group_id}",
            response_type=models.material.MaterialGroupResponse,
        )

    def get_material_groups(
        self,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.material.MaterialGroupResponse]:
        """List all the material groups the user has access to"""
        data = self._client.request(
            "GET",
            "/materialgroups",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.material.MaterialGroupResponse)

    def get_materials(
        self,
        material_group_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.material.MaterialResponse]:
        """List materials within the material group"""
        data = self._client.request(
            "GET",
            f"/materialgroups/{material_group_id}/materials",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.material.MaterialResponse)

    def get_nested_material_groups(
        self,
        material_group_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.material.MaterialGroupResponse]:
        """List all sub-groups of the specified material group"""
        data = self._client.request(
            "GET",
            f"/materialgroups/{material_group_id}/materialgroups",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.material.MaterialGroupResponse)

    def update_material_data(
        self,
        material_group_id: str,
        material_id: str,
        body: models.material.CreateMaterialRequest,
    ) -> models.material.MaterialResponse:
        """Update an existing material"""
        return self._client.request(
            "PUT",
            f"/materialgroups/{material_group_id}/materials/{material_id}",
            json_body=body,
            response_type=models.material.MaterialResponse,
        )

    def update_material_group_metadata(
        self,
        material_group_id: str,
        body: models.material.UpdateMaterialGroupRequest,
    ) -> models.material.MaterialGroupResponse:
        """Update material group information"""
        return self._client.request(
            "PUT",
            f"/materialgroups/{material_group_id}",
            json_body=body,
            response_type=models.material.MaterialGroupResponse,
        )
