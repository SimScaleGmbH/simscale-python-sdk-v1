from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class SimulationRuns:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def add_wind_data_to_simulation_run(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        body: models.WindData,
    ) -> models.SimulationRun:
        """Add wind data to a simulation run (works only for PWC runs)



        You can use this endpoint to add wind data to an existing PWC run. This means that for the new run, only the statistical surface solution will be regenerated based on the new wind data, while the individual results of each direction will be kept from the original run. This endpoint is only used to trigger the execution of the new simulation run - before calling this endpoint make sure to update the simulation spec with the new wind data.
        """
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/add-wind-data",
            json_body=body,
            response_type=models.SimulationRun,
        )

    def cancel_simulation_run(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
    ) -> None:
        """Cancel the simulation run"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/cancel",
        )

    def cancel_simulation_run_sub_run(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        sub_run_id: str,
    ) -> None:
        """Cancel the sub-run of a parametric run"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/subruns/{sub_run_id}/cancel",
        )

    def create_simulation_run(
        self,
        project_id: str,
        simulation_id: str,
        body: models.SimulationRun,
    ) -> models.SimulationRun:
        """Create a simulation run



        This operation creates a run in status `READY`, however the run is not automatically started. The run must be started explicitly using the `POST /projects/{projectId}/simulations/{simulationId}/runs/{runId}/start` endpoint.
        """
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/runs",
            json_body=body,
            response_type=models.SimulationRun,
        )

    def delete_simulation_run_sub_run(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        sub_run_id: str,
    ) -> None:
        """Delete the sub-run of a parametric run"""
        return self._client.request(
            "DELETE",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/subruns/{sub_run_id}",
        )

    def get_simulation_run(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
    ) -> models.SimulationRun:
        """Get basic information about the simulation run"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}",
            response_type=models.SimulationRun,
        )

    def get_simulation_run_event_log(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
    ) -> models.EventLogResponse:
        """Get the simulation run event log"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/eventlog",
            response_type=models.EventLogResponse,
        )

    def get_simulation_run_results(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        type_: str | None = None,
        category: str | None = None,
        quantity: str | None = None,
        name: str | None = None,
        direction: str | None = None,
    ) -> PaginatedResponse[models.OneOfSimulationRunResult]:
        """List available results for a simulation runs"""
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/results",
            query_params={
                "limit": limit,
                "page": page,
                "type": type_,
                "category": category,
                "quantity": quantity,
                "name": name,
                "direction": direction,
            },
        )
        return PaginatedResponse(data, models.OneOfSimulationRunResult)

    def get_simulation_run_spec(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        *,
        simulation_spec_schema_version: str | None = None,
    ) -> models.SimulationSpec:
        """Get the simulation run spec"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/spec",
            query_params={"simulationSpecSchemaVersion": simulation_spec_schema_version},
            response_type=models.SimulationSpec,
        )

    def get_simulation_run_sub_run_results(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        sub_run_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        type_: str | None = None,
        category: str | None = None,
        quantity: str | None = None,
        name: str | None = None,
    ) -> PaginatedResponse[models.OneOfSimulationRunResult]:
        """Get the simulation sub-run results"""
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/subruns/{sub_run_id}/results",
            query_params={
                "limit": limit,
                "page": page,
                "type": type_,
                "category": category,
                "quantity": quantity,
                "name": name,
            },
        )
        return PaginatedResponse(data, models.OneOfSimulationRunResult)

    def get_simulation_run_sub_run_spec(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        sub_run_id: str,
        *,
        simulation_spec_schema_version: str | None = None,
    ) -> models.SimulationSpec:
        """Get the simulation sub-run spec"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/subruns/{sub_run_id}/spec",
            query_params={"simulationSpecSchemaVersion": simulation_spec_schema_version},
            response_type=models.SimulationSpec,
        )

    def get_simulation_run_sub_runs(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.SimulationRun]:
        """List of sub-runs of parametric runs"""
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/subruns",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.SimulationRun)

    def get_simulation_runs(
        self,
        project_id: str,
        simulation_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.SimulationRun]:
        """List simulation runs for a simulation"""
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/simulations/{simulation_id}/runs",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.SimulationRun)

    def start_simulation_run(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
    ) -> None:
        """Start the simulation run"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}/start",
        )

    def update_simulation_run(
        self,
        project_id: str,
        simulation_id: str,
        run_id: str,
        body: models.SimulationRun,
    ) -> None:
        """Update an existing simulation run"""
        return self._client.request(
            "PUT",
            f"/projects/{project_id}/simulations/{simulation_id}/runs/{run_id}",
            json_body=body,
        )
