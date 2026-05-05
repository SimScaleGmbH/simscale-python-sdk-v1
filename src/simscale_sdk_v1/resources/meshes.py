from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Meshes:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_mesh(
        self,
        project_id: str,
        mesh_id: str,
    ) -> models.Mesh:
        """Get information about the mesh"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/meshes/{mesh_id}",
            response_type=models.Mesh,
        )

    def get_meshes(
        self,
        project_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.Mesh]:
        """List meshes within a project



        Only finished and non-uploaded meshes are included.
        """
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/meshes",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.Mesh)
