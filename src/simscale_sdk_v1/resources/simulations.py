from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Simulations:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def check_simulation_setup(
        self,
        project_id: str,
        simulation_id: str,
    ) -> models.CheckResponse:
        """Check the simulation setup"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/check",
            response_type=models.CheckResponse,
        )

    def create_geometry_primitive(
        self,
        project_id: str,
        body: models.geometry_primitive.GeometryPrimitive,
    ) -> models.GeometryPrimitiveResponse:
        """Create a geometry primitive for reference within a Simulation spec"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/geometryprimitives",
            json_body=body,
            response_type=models.GeometryPrimitiveResponse,
        )

    def create_simulation(
        self,
        project_id: str,
        body: models.SimulationSpec,
    ) -> models.simulation.Simulation:
        """Create a simulation setup"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations",
            json_body=body,
            response_type=models.simulation.Simulation,
        )

    def estimate_simulation_setup(
        self,
        project_id: str,
        simulation_id: str,
    ) -> models.Estimation:
        """Estimate the simulation setup"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/estimate",
            response_type=models.Estimation,
        )

    def get_simulation(
        self,
        project_id: str,
        simulation_id: str,
        *,
        simulation_spec_schema_version: str | None = None,
    ) -> models.SimulationSpec:
        """Get information about the simulation setup"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}",
            query_params={"simulationSpecSchemaVersion": simulation_spec_schema_version},
            response_type=models.SimulationSpec,
        )

    def get_simulations(
        self,
        project_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.simulation.Simulation]:
        """List simulation setups within a project"""
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/simulations",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.simulation.Simulation)

    def swap_simulation_cad(
        self,
        project_id: str,
        simulation_id: str,
        body: models.SwapCadRequest,
    ) -> models.SwapCadReport:
        """Swap the CAD on which the simulation is based



        Swap the CAD on which the simulation is based. The assignments on CAD entities are mapped accordingly.

        This operation supports only swap between two CADs.
        """
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/swapcad",
            json_body=body,
            response_type=models.SwapCadReport,
        )

    def update_simulation(
        self,
        project_id: str,
        simulation_id: str,
        body: models.SimulationSpec,
    ) -> None:
        """Update information about the simulation setup"""
        return self._client.request(
            "PUT",
            f"/projects/{project_id}/simulations/{simulation_id}",
            json_body=body,
        )

    def update_simulation_materials(
        self,
        project_id: str,
        simulation_id: str,
        body: models.MaterialUpdateRequest,
        *,
        preview: bool | None = None,
    ) -> models.MaterialUpdateResponse:
        """Update materials in the simulation setup"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/materials",
            json_body=body,
            query_params={"preview": preview},
            response_type=models.MaterialUpdateResponse,
        )
