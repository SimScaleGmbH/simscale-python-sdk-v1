from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Cads:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_cad_state_saved_selection(
        self,
        cad_id: str,
        cad_state_id: str,
        body: models.CreateSavedSelectionRequest,
    ) -> models.CreateSavedSelectionResponse:
        """Create a CAD saved selection



        Create a CAD saved selection. This operation creates a new CAD state.
        """
        return self._client.request(
            "POST",
            f"/cads/{cad_id}/states/{cad_state_id}/savedselections",
            json_body=body,
            response_type=models.CreateSavedSelectionResponse,
        )

    def download_original_cad(
        self,
        cad_id: str,
        cad_state_id: str,
    ) -> models.DownloadOriginalCadResponse:
        """Download original CAD file



        Get a temporary link to download the originally imported CAD file.
        """
        return self._client.request(
            "GET",
            f"/cads/{cad_id}/states/{cad_state_id}/downloadoriginal",
            response_type=models.DownloadOriginalCadResponse,
        )

    def get_cad(
        self,
        project_id: str,
        cad_id: str,
    ) -> models.cad.Cad:
        """Get information about the CAD"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/cads/{cad_id}",
            response_type=models.cad.Cad,
        )

    def get_cad_state(
        self,
        cad_id: str,
        cad_state_id: str,
    ) -> models.CadState:
        """Get detailed information about the CAD state"""
        return self._client.request(
            "GET",
            f"/cads/{cad_id}/states/{cad_state_id}",
            response_type=models.CadState,
        )

    def get_cad_topology(
        self,
        cad_id: str,
        cad_state_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        class_: str | None = None,
        bodies: list[str] | None = None,
        entities: list[str] | None = None,
        attributes: list[str] | None = None,
        values: list[str] | None = None,
    ) -> models.CadTopology:
        """List CAD topology with entity attributes



        Assignment of topological entities (e.g. faces, bodies) in the simulation setup is a non-trivial task.

        Complex models can consist of several assemblies which may contain multiple occurrences of bodies and their entities.

        In order to identify an assignment unambiguously, the full path from the root part of the model to the actual topological entity is required.



        SimScale generates unique internal names for all topological entities of a model during the CAD import which are used for assignments within the simulation spec.

        Examples of internal names are `B1_TE5` or `A1_I26_A5_I27_B102_TE196`.



        This API endpoint lists the CAD model’s topology with all relevant attributes for each entity, such as:

        * The topological entity class (body or face)

        * The original body and entity names

        * Entity attributes like `SDL/TYSA_NAME`, `SDL/TYSA_UNAME`, `ATTRIB_XPARASOLID_NAME` or `SDL/TYSA_COLOUR`

        * The path from the root of the model



        Please note that during the CAD import the model's topology can be modified (e.g. when the facet split option is enabled).

        This means that there might not be a 1:1 mapping between the internal and original names.
        """
        return self._client.request(
            "GET",
            f"/cads/{cad_id}/states/{cad_state_id}/topology",
            query_params={
                "limit": limit,
                "page": page,
                "class": class_,
                "bodies": bodies,
                "entities": entities,
                "attributes": attributes,
                "values": values,
            },
            response_type=models.CadTopology,
        )

    def get_cads(
        self,
        project_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> models.Cads:
        """List CADs within a project



        All CADs in the project are included in the list, however not all of them can be used in a meshing or simulation setup.
        """
        return self._client.request(
            "GET",
            f"/projects/{project_id}/cads",
            query_params={"limit": limit, "page": page},
            response_type=models.Cads,
        )

    def query_cad_state(
        self,
        cad_id: str,
        cad_state_id: str,
        body: models.cad.CadQueryRequest,
    ) -> models.CadQueryResponse:
        """Run a CAD query



        Run a CAD query on a given CAD state. CAD queries that involve complex computation might take some time to complete.

        Please refer to the following steps to run a CAD query:

        1. Trigger the query computation via `POST /cads/{cadId}/states/{cadStateId}/query`

        2. Monitor progress via `POST /cads/{cadId}/states/{cadStateId}/query`
        """
        return self._client.request(
            "POST",
            f"/cads/{cad_id}/states/{cad_state_id}/query",
            json_body=body,
            response_type=models.CadQueryResponse,
        )

    def rename_cad_state(
        self,
        cad_id: str,
        cad_state_id: str,
        body: models.RenameCadRequest,
    ) -> models.RenameCadResponse:
        """Rename the CAD



        Rename the CAD. This operation creates a new CAD state.
        """
        return self._client.request(
            "POST",
            f"/cads/{cad_id}/states/{cad_state_id}/rename",
            json_body=body,
            response_type=models.RenameCadResponse,
        )
