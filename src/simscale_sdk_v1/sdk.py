"""SimScaleSDK entry point — generated resource wiring + helpers."""

from __future__ import annotations

import os

from simscale_sdk_v1.client import SimScaleClient
from simscale_sdk_v1.helpers import SimScaleHelpers
from simscale_sdk_v1.resources.ai_models import AiModels
from simscale_sdk_v1.resources.cad_features import CadFeatures
from simscale_sdk_v1.resources.cad_imports import CadImports
from simscale_sdk_v1.resources.cads import Cads
from simscale_sdk_v1.resources.component_registry import ComponentRegistry
from simscale_sdk_v1.resources.data_repository import DataRepository
from simscale_sdk_v1.resources.export import Export
from simscale_sdk_v1.resources.folders import Folders
from simscale_sdk_v1.resources.materials import Materials
from simscale_sdk_v1.resources.mesh_operations import MeshOperations
from simscale_sdk_v1.resources.meshes import Meshes
from simscale_sdk_v1.resources.postprocessing import Postprocessing
from simscale_sdk_v1.resources.project_permissions import ProjectPermissions
from simscale_sdk_v1.resources.projects import Projects
from simscale_sdk_v1.resources.reports import Reports
from simscale_sdk_v1.resources.simulation_runs import SimulationRuns
from simscale_sdk_v1.resources.simulations import Simulations
from simscale_sdk_v1.resources.space_permissions import SpacePermissions
from simscale_sdk_v1.resources.spaces import Spaces
from simscale_sdk_v1.resources.storage import Storage
from simscale_sdk_v1.resources.table_imports import TableImports
from simscale_sdk_v1.resources.users import Users
from simscale_sdk_v1.resources.wind import Wind
from simscale_sdk_v1.resources.workflow_repository import WorkflowRepository
from simscale_sdk_v1.resources.workflow_runner import WorkflowRunner

_DEFAULT_URL = "https://api.simscale.com"


class SimScaleSDK(SimScaleHelpers):
    def __init__(
        self,
        *,
        api_key: str | None = None,
        server_url: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 5,
        max_connections: int = 100,
        max_requests_per_second: float | None = None,
    ) -> None:
        resolved_key = api_key or os.environ.get("SIMSCALE_API_KEY")
        if not resolved_key:
            raise ValueError("api_key must be provided or SIMSCALE_API_KEY environment variable must be set")
        resolved_url = (server_url or os.environ.get("SIMSCALE_API_URL", _DEFAULT_URL)).rstrip("/") + "/v1"
        self._client = SimScaleClient(
            api_key=resolved_key,
            server_url=resolved_url,
            timeout=timeout,
            max_retries=max_retries,
            max_connections=max_connections,
            max_requests_per_second=max_requests_per_second,
        )

        self.ai_models = AiModels(self._client)
        self.cad_features = CadFeatures(self._client)
        self.cad_imports = CadImports(self._client)
        self.cads = Cads(self._client)
        self.component_registry = ComponentRegistry(self._client)
        self.data_repository = DataRepository(self._client)
        self.export = Export(self._client)
        self.folders = Folders(self._client)
        self.materials = Materials(self._client)
        self.mesh_operations = MeshOperations(self._client)
        self.meshes = Meshes(self._client)
        self.postprocessing = Postprocessing(self._client)
        self.project_permissions = ProjectPermissions(self._client)
        self.projects = Projects(self._client)
        self.reports = Reports(self._client)
        self.simulation_runs = SimulationRuns(self._client)
        self.simulations = Simulations(self._client)
        self.space_permissions = SpacePermissions(self._client)
        self.spaces = Spaces(self._client)
        self.storage = Storage(self._client)
        self.table_imports = TableImports(self._client)
        self.users = Users(self._client)
        self.wind = Wind(self._client)
        self.workflow_repository = WorkflowRepository(self._client)
        self.workflow_runner = WorkflowRunner(self._client)
