from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class MeshOperations:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def cancel_mesh_operation(
        self,
        project_id: str,
        mesh_operation_id: str,
    ) -> None:
        """Cancel the mesh operation"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}/cancel",
        )

    def check_mesh_operation_setup(
        self,
        project_id: str,
        mesh_operation_id: str,
        *,
        simulation_id: str | None = None,
    ) -> models.CheckResponse:
        """Check the mesh operation setup"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}/check",
            query_params={"simulationId": simulation_id},
            response_type=models.CheckResponse,
        )

    def create_mesh_operation(
        self,
        project_id: str,
        body: models.MeshOperation,
    ) -> models.MeshOperation:
        """Create a mesh operation"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/meshoperations",
            json_body=body,
            response_type=models.MeshOperation,
        )

    def estimate_mesh_operation(
        self,
        project_id: str,
        mesh_operation_id: str,
    ) -> models.Estimation:
        """Estimate the mesh operation"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}/estimate",
            response_type=models.Estimation,
        )

    def get_mesh_operation(
        self,
        project_id: str,
        mesh_operation_id: str,
        *,
        meshing_spec_schema_version: str | None = None,
    ) -> models.MeshOperation:
        """Get information about the mesh operation"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}",
            query_params={"meshingSpecSchemaVersion": meshing_spec_schema_version},
            response_type=models.MeshOperation,
        )

    def get_mesh_operation_event_log(
        self,
        project_id: str,
        mesh_operation_id: str,
    ) -> models.EventLogResponse:
        """Get the mesh operation event log"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}/eventlog",
            response_type=models.EventLogResponse,
        )

    def get_mesh_operations(
        self,
        project_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.SlimMeshOperation]:
        """List mesh operations for a project"""
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/meshoperations",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.SlimMeshOperation)

    def start_mesh_operation(
        self,
        project_id: str,
        mesh_operation_id: str,
        *,
        simulation_id: str | None = None,
    ) -> None:
        """Start the mesh operation"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}/start",
            query_params={"simulationId": simulation_id},
        )

    def swap_mesh_operation_cad(
        self,
        project_id: str,
        mesh_operation_id: str,
        body: models.SwapCadRequest,
    ) -> models.SwapCadReport:
        """Swap the CAD on which the mesh is based



        Swap the CAD on which the mesh is based. The assignments on CAD entities are mapped accordingly.
        """
        return self._client.request(
            "POST",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}/swapcad",
            json_body=body,
            response_type=models.SwapCadReport,
        )

    def update_mesh_operation(
        self,
        project_id: str,
        mesh_operation_id: str,
        body: models.MeshOperation,
    ) -> None:
        """Update information about the mesh operation"""
        return self._client.request(
            "PUT",
            f"/projects/{project_id}/meshoperations/{mesh_operation_id}",
            json_body=body,
        )
