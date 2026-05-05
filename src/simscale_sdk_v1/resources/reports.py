from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Reports:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def cancel_report_job(
        self,
        project_id: str,
        report_id: str,
    ) -> None:
        return self._client.request(
            "POST",
            f"/projects/{project_id}/reports/{report_id}/cancel",
        )

    def create_report(
        self,
        project_id: str,
        body: models.reporting.ReportRequest,
    ) -> models.reporting.ReportResponse:
        return self._client.request(
            "POST",
            f"/projects/{project_id}/reports",
            json_body=body,
            response_type=models.reporting.ReportResponse,
        )

    def create_report_from_postprocessing_state(
        self,
        project_id: str,
        body: models.reporting.ReportFromStateRequest,
    ) -> models.reporting.ReportResponse:
        return self._client.request(
            "POST",
            f"/projects/{project_id}/reports/from-state",
            json_body=body,
            response_type=models.reporting.ReportResponse,
        )

    def delete_report(
        self,
        project_id: str,
        report_id: str,
    ) -> None:
        return self._client.request(
            "DELETE",
            f"/projects/{project_id}/reports/{report_id}",
        )

    def get_report(
        self,
        project_id: str,
        report_id: str,
    ) -> models.reporting.ReportResponse:
        return self._client.request(
            "GET",
            f"/projects/{project_id}/reports/{report_id}",
            response_type=models.reporting.ReportResponse,
        )

    def get_reports(
        self,
        project_id: str,
        *,
        simulation_id: str | None = None,
        run_id: str | None = None,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.reporting.ReportResponse]:
        data = self._client.request(
            "GET",
            f"/projects/{project_id}/reports",
            query_params={"simulationId": simulation_id, "runId": run_id, "limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.reporting.ReportResponse)

    def start_report_job(
        self,
        project_id: str,
        report_id: str,
    ) -> None:
        return self._client.request(
            "POST",
            f"/projects/{project_id}/reports/{report_id}/start",
        )

    def update_report(
        self,
        project_id: str,
        report_id: str,
        body: models.reporting.ReportRequest,
    ) -> None:
        return self._client.request(
            "PUT",
            f"/projects/{project_id}/reports/{report_id}",
            json_body=body,
        )
