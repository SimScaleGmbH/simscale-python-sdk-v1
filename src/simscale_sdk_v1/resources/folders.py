from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Folders:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_folder(
        self,
        space_id: str,
        body: models.Folder,
    ) -> models.Folder:
        """Create Folder



        Create a new Folder. If `parentFolderId` is missing, the folder will be created at the root level of the Space. Folder name clashes are allowed.
        """
        return self._client.request(
            "POST",
            f"/spaces/{space_id}/folders",
            json_body=body,
            response_type=models.Folder,
        )

    def delete_folder(
        self,
        space_id: str,
        folder_id: str,
    ) -> None:
        """Delete Folder



        Delete a folder and all its content. The deletion is propagated to all child elements. If the total number of elements to delete is too large, this operation will be carried out asynchronously.
        """
        return self._client.request(
            "DELETE",
            f"/spaces/{space_id}/folders/{folder_id}",
        )

    def get_folder_info(
        self,
        space_id: str,
        folder_id: str,
    ) -> models.Folder:
        """Get Folder Info



        Get Folder metadata and current user permissions.
        """
        return self._client.request(
            "GET",
            f"/spaces/{space_id}/folders/{folder_id}",
            response_type=models.Folder,
        )

    def list_folders_in_folder(
        self,
        space_id: str,
        folder_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
    ) -> PaginatedResponse[models.Folder]:
        """List Folders in Folder



        List folders located in a Folder. Filtering or search capabilities are not supported. This only returns the folders of the queried folder, without a recursive expansion to child folders
        """
        data = self._client.request(
            "GET",
            f"/spaces/{space_id}/folders/{folder_id}/content/folders",
            query_params={"limit": limit, "page": page, "sort": sort},
        )
        return PaginatedResponse(data, models.Folder)

    def list_folders_in_space_root(
        self,
        space_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
    ) -> PaginatedResponse[models.Folder]:
        """List Folders in Space root



        List folders located at the root level of a Space. Filtering or search capabilities are not supported. This only returns the folders at the root level of a Space, without a recursive expansion to child folders.
        """
        data = self._client.request(
            "GET",
            f"/spaces/{space_id}/content/folders",
            query_params={"limit": limit, "page": page, "sort": sort},
        )
        return PaginatedResponse(data, models.Folder)

    def list_projects_in_folder(
        self,
        space_id: str,
        folder_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
    ) -> PaginatedResponse[models.Project]:
        """List Projects in Folder



        List projects located in a Folder. Filtering or search capabilities are not supported. This only returns the projects of the queried folder, without a recursive expansion to child folders.
        """
        data = self._client.request(
            "GET",
            f"/spaces/{space_id}/folders/{folder_id}/content/projects",
            query_params={"limit": limit, "page": page, "sort": sort},
        )
        return PaginatedResponse(data, models.Project)

    def list_projects_in_space_root(
        self,
        space_id: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
    ) -> PaginatedResponse[models.Project]:
        """List Projects in Space root



        List projects located at the root level of a Space. Filtering or search capabilities are not supported. This only returns the projects at the root level of a Space, without a recursive expansion to child folders.
        """
        data = self._client.request(
            "GET",
            f"/spaces/{space_id}/content/projects",
            query_params={"limit": limit, "page": page, "sort": sort},
        )
        return PaginatedResponse(data, models.Project)

    def move_content_from_folder(
        self,
        space_id: str,
        folder_id: str,
        body: models.MoveContentRequest,
    ) -> None:
        """Move Content from Folder



        Move content from this folder. Several resources can be moved with the same request. All resources must be moved to the same target location. Folders cannot be moved to a different Space. Projects can only be moved to a Personal Space if the Space owner and the project owner match.
        """
        return self._client.request(
            "POST",
            f"/spaces/{space_id}/folders/{folder_id}/move",
            json_body=body,
        )

    def move_content_from_space_root(
        self,
        space_id: str,
        body: models.MoveContentRequest,
    ) -> None:
        """Move Content from Space root



        Move content located at the root level of a Space. Several resources can be moved with the same request. All resources must be moved to the same target location. Folders cannot be moved to a different Space. Projects can only be moved to a Personal Space if the Space owner and the project owner match.
        """
        return self._client.request(
            "POST",
            f"/spaces/{space_id}/move",
            json_body=body,
        )

    def update_folder(
        self,
        space_id: str,
        folder_id: str,
        body: models.Folder,
    ) -> models.Folder:
        """Update Folder



        Update Folder metadata
        """
        return self._client.request(
            "PUT",
            f"/spaces/{space_id}/folders/{folder_id}",
            json_body=body,
            response_type=models.Folder,
        )
