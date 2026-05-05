# Migrating from v0 SDK

For new code or a thorough migration, use the native v1 API directly.

## 1. Setup & Initialization

The v0 boilerplate (Configuration, ApiClient, retry policy, individual API class instances) is replaced by a single `SimScaleSDK` entry point.

```python
# v0
from simscale_sdk import Configuration, ApiClient, ProjectsApi, SimulationsApi, ...

configuration = Configuration()
configuration.host = api_url + "/v0"
configuration.api_key = {"X-API-KEY": api_key}
api_client = ApiClient(configuration)

retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
api_client.rest_client.pool_manager.connection_pool_kw["retries"] = retry_policy

project_api = ProjectsApi(api_client)
simulation_api = SimulationsApi(api_client)
mesh_operation_api = MeshOperationsApi(api_client)

# v1
from simscale_sdk_v1 import SimScaleSDK
sdk = SimScaleSDK(api_key=api_key)  # defaults to https://api.simscale.com
```

## 2. Package & Imports

v0 imported all model classes from a single flat namespace. v1 organizes models into domain-specific submodules:

```python
# v0
from simscale_sdk import Project, SimulationSpec, WindComfort, DimensionalLength, ...

# v1 — core models
from simscale_sdk_v1 import SimScaleSDK, SimScaleAPIError, SimScaleOperationError, models

# v1 — domain-specific submodule aliases (recommended for simulation/meshing/reporting models)
from simscale_sdk_v1.models import simulation as sim
from simscale_sdk_v1.models import meshing as mesh
from simscale_sdk_v1.models import reporting as rpt
from simscale_sdk_v1.models import geometry_primitive as geo
```

Then use `models.Project(...)` for core API models and `sim.WindComfort(...)`, `mesh.SimmetrixMeshingFluid(...)`, etc. for domain models. Available submodules: `simulation`, `meshing`, `reporting`, `geometry_primitive`, `material`, `cad`, `postprocessing`, `parametric`.

## 3. API Resource Mapping

Replace individual API class instances with SDK attributes:

| v0 | v1 |
|----|-----|
| `project_api = ProjectsApi(api_client)` | `sdk.projects` |
| `geometry_import_api = GeometryImportsApi(api_client)` | `sdk.cad_imports` |
| `geometry_api = GeometriesApi(api_client)` | `sdk.cads` |
| `mesh_operation_api = MeshOperationsApi(api_client)` | `sdk.mesh_operations` |
| `simulation_api = SimulationsApi(api_client)` | `sdk.simulations` |
| `simulation_run_api = SimulationRunsApi(api_client)` | `sdk.simulation_runs` |
| `materials_api = MaterialsApi(api_client)` | `sdk.materials` |
| `reports_api = ReportsApi(api_client)` | `sdk.reports` |
| `storage_api = StorageApi(api_client)` | `sdk.storage` |
| `table_import_api = TableImportsApi(api_client)` | `sdk.table_imports` |
| `wind_api = WindApi(api_client)` | `sdk.wind` |

## 4. Method Calling Convention

Method signatures are the same as v0: path params and body are positional args, query params are keyword args. The only difference is the receiver (`simulation_api` → `sdk.simulations`).

```python
# v0
simulation_api.create_simulation(project_id, simulation_spec)
mesh_operation_api.check_mesh_operation_setup(project_id, mesh_op_id, simulation_id=sim_id)

# v1
sdk.simulations.create_simulation(project_id, simulation_spec)
sdk.mesh_operations.check_mesh_operation_setup(project_id, mesh_op_id, simulation_id=sim_id)
```

In v0, the body parameter had method-specific names (`project=`, `folder=`, etc.). In v1, it is always `body` when passed as a keyword argument. Since body is a positional arg, you typically don't need to name it:

```python
# v0 (keyword)
folders_api.create_folder(space_id=space_id, folder=Folder(name="A"))

# v1 (positional — recommended)
sdk.folders.create_folder(space_id, Folder(name="A"))
```

## 5. API Renames (geometry → cad)

The v1 API renamed geometry-related endpoints to CAD:

| v0 | v1 |
|----|-----|
| `geometry_import_api.import_geometry(...)` | `sdk.cad_imports.import_cad(...)` |
| `geometry_import_api.get_geometry_import(...)` | `sdk.cad_imports.get_imported_cad(...)` |
| `geometry_api.get_geometry_mappings(...)` | `sdk.cads.get_cad_topology(...)` |
| `geometry_import.geometry_id` | `cad_import.cad_id` |
| `MeshOperation(..., geometry_id=gid)` | `MeshOperation(..., cad_id=cid, state_id=sid)` |
| `SimulationSpec(..., geometry_id=gid)` | `SimulationSpec(..., cad_id=cid, state_id=sid)` |

In v1, a CAD import returns both `cad_id` and `cad_state_id`. Both must be passed to `SimulationSpec` and `MeshOperation` — `cad_id` identifies the CAD model, `state_id` identifies its specific version/state.

## 6. Model Class Renames

The v1 SDK uses schema names directly from the OpenAPI spec, which include underscores that v0 stripped:

| v0 | v1 |
|----|-----|
| `DimensionalLength` | `Dimensional_Length` |
| `DimensionalAngle` | `Dimensional_Angle` |
| `DimensionalPressure` | `Dimensional_Pressure` |
| `DimensionalTime` | `Dimensional_Time` |
| `DimensionalVectorLength` | `DimensionalVector_Length` |
| `DimensionalVector2dLength` | `DimensionalVector2d_Length` |
| `DimensionalVectorFunctionSpeed` | `DimensionalVectorFunction_Speed` |
| `DimensionalFunctionPressure` | `DimensionalFunction_Pressure` |
| `DimensionalFunctionSpeed` | `DimensionalFunction_Speed` |
| `DimensionalFunctionDimensionless` | `DimensionalFunction_Dimensionless` |
| `DimensionalFunctionSpecificTurbulenceDissipationRate` | `DimensionalFunction_SpecificTurbulenceDissipationRate` |
| `DimensionalVectorAngle` | `DimensionalVector_Angle` |

General pattern: where the OpenAPI schema name contains an underscore (e.g., `Dimensional_Pressure`), v0 removed it (`DimensionalPressure`) while v1 preserves it. This applies to all `Dimensional*` classes.

## 7. CAD Import Request Models

The v0 geometry import request classes were renamed to CAD (not removed). The constructor uses keyword arguments:

| v0 | v1 |
|----|-----|
| `GeometryImportRequestLocation(storage_id)` | `CadImportRequestLocation(storage_id=storage_id)` |
| `GeometryImportRequestOptions(facet_split=False, ...)` | `CadImportRequestOptions(facet_split=False, ...)` |
| `GeometryImportRequest(...)` | `CadImportRequest(...)` |

## 8. Python Keyword Conflicts

Some model fields whose JSON name is a Python keyword use a trailing underscore in v1 (v0 used a leading underscore):

| v0 | v1 |
|----|-----|
| `WindRoseVelocityBucket(_from=1.0, ...)` | `WindRoseVelocityBucket(from_=1.0, ...)` |

## 9. Enum Classes → String Literals

v0 generated enum classes; v1 uses string literals (matching the API values):

| v0 | v1 |
|----|-----|
| `MaterialGroupType.SIMSCALE_DEFAULT` | `"SIMSCALE_DEFAULT"` |
| `ProjectionType.ORTHOGONAL` | `"ORTHOGONAL"` |
| `RenderMode.SURFACES` | `"SURFACES"` |

## 10. Pagination

| v0 | v1 |
|----|-----|
| `result.meta.total` | `result.total` |
| `result.embedded` | `result.embedded` (unchanged) |

## 11. File Upload & Download

v0 used the internal `api_client.rest_client` for HTTP calls. v1 provides `upload()` and `download()` helpers:

```python
# Upload (v0)
storage = storage_api.create_storage()
api_client.rest_client.PUT(url=storage.url, headers={...}, body=file.read())
# Upload (v1)
storage = sdk.upload("model.stl")

# Download (v0)
response = api_client.rest_client.GET(url=url, headers={...}, _preload_content=False)
with open("result.csv", "wb") as f:
    f.write(response.data)
# Download (v1)
sdk.download(url, "result.csv")
```

## 12. Table Imports

Table import follows the same upload-then-import pattern as CAD imports. The model classes (`TableImportRequest`, `TableImportRequestLocation`) are in the core `models` namespace:

```python
# v0
table_csv_storage = storage_api.create_storage()
with open("data.csv", "rb") as f:
    api_client.rest_client.PUT(url=table_csv_storage.url, headers={...}, body=f.read())
table_import = table_import_api.import_table(
    project_id, TableImportRequest(location=TableImportRequestLocation(table_csv_storage.storage_id))
)
table_id = table_import.table_id

# v1
table_storage = sdk.upload("data.csv")
table_import = sdk.table_imports.import_table(
    project_id,
    models.TableImportRequest(location=models.TableImportRequestLocation(storage_id=table_storage.storage_id)),
)
table_id = table_import.table_id
```

Note: `TableImportRequestLocation` in v1 uses keyword argument `storage_id=` (v0 used a positional argument).

## 13. Geometry Primitives

Geometry primitive classes (`RotatableCartesianBox`, `LocalCartesianBox`, `Point`, etc.) are in the `geometry_primitive` submodule:

```python
from simscale_sdk_v1.models import geometry_primitive as geo

# v0
external_flow_domain = RotatableCartesianBox(
    name="External Flow Domain",
    min=DimensionalVectorLength(value=DecimalVector(x=-350, y=-100, z=0), unit="m"),
    ...
)
uuid = simulation_api.create_geometry_primitive(project_id, external_flow_domain).geometry_primitive_id

# v1
external_flow_domain = sdk.simulations.create_geometry_primitive(
    project_id,
    geo.RotatableCartesianBox(
        name="External Flow Domain",
        min=geo.DimensionalVector_Length(value=geo.DecimalVector(x=-350, y=-100, z=0), unit="m"),
        ...
    ),
)
uuid = external_flow_domain.geometry_primitive_id
```

Note: geometry primitive model classes like `DimensionalVector_Length`, `DecimalVector`, and `DimensionalVector_Angle` exist in both the `simulation` and `geometry_primitive` submodules. Use the submodule that matches the context (`geo.` for geometry primitives, `sim.` for simulation models).

## 14. Error Handling

| v0 | v1 |
|----|-----|
| `from simscale_sdk import ApiException` | `from simscale_sdk_v1 import SimScaleAPIError` |
| `except ApiException as e:` | `except SimScaleAPIError as e:` |
| `e.status` | `e.status_code` |
| `e.body` | `e.body` |

v1 also adds `SimScaleOperationError`, raised automatically by `sdk.wait_until_done()` when an operation finishes with a failure status. You can also raise it manually for setup check failures:

```python
from simscale_sdk_v1 import SimScaleOperationError

check = sdk.simulations.check_simulation_setup(project_id, simulation_id)
if any(e.severity == "ERROR" for e in check.entries):
    raise SimScaleOperationError(check, "Simulation setup check failed")
```

## 15. Result Downloads via Export API

In v0, some simulation run results (e.g., `STATISTICAL_SURFACE_SOLUTION`) had a `download.url` field for direct download. In v1, all result downloads go through the Export API:

```python
# v0: direct download from result
results = simulation_run_api.get_simulation_run_results(project_id, simulation_id, run_id, category="SOLUTION")
result = results.embedded[0]
response = api_client.rest_client.GET(url=result.download.url, headers={...}, _preload_content=False)

# v1: create an export, wait for it, then download
results = sdk.simulation_runs.get_simulation_run_results(project_id, simulation_id, run_id, category="SOLUTION")
result = results.embedded[0]
export = sdk.export.create_export(
    project_id, models.CreateExportRequest(result_id=result.result_id, format="VTK")
)
export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, export.export_id), interval=5)
sdk.download(export.url, "result.zip")
```

## 16. Polling Loops → `wait_until_done`

v0 examples used manual `while` loops with `time.sleep()` and `time.time()` for timeout tracking. v1 replaces all of these with `sdk.wait_until_done()`:

```python
# v0
import time
geometry_import_start = time.time()
while geometry_import.status not in ("FINISHED", "CANCELED", "FAILED"):
    if time.time() > geometry_import_start + 900:
        raise TimeoutError()
    time.sleep(10)
    geometry_import = geometry_import_api.get_geometry_import(project_id, geometry_import_id)

# v1
cad_import = sdk.wait_until_done(
    lambda: sdk.cad_imports.get_imported_cad(project_id, cad_id),
    timeout=900, interval=10,
)
```

This applies to CAD imports, mesh operations, simulation runs, exports, and reports. The method raises `SimScaleOperationError` on failure and `TimeoutError` on timeout.

## Quick Migration Checklist

1. [ ] Replace `Configuration` + `ApiClient` + `XxxApi(...)` boilerplate with `SimScaleSDK()`
2. [ ] Change imports from `simscale_sdk` to `simscale_sdk_v1` (use domain submodule aliases like `simulation as sim`)
3. [ ] Replace `xxx_api.method(...)` with `sdk.resource.method(...)`
4. [ ] Rename `geometry` → `cad` (imports, API calls, model fields)
5. [ ] Add `state_id` to `SimulationSpec` and `MeshOperation` (from CAD import's `cad_state_id`)
6. [ ] Update model class names with underscores (e.g., `DimensionalPressure` → `Dimensional_Pressure`)
7. [ ] Rename `GeometryImportRequest*` classes to `CadImportRequest*`
8. [ ] Update Python keyword fields: `_from` → `from_` (e.g., `WindRoseVelocityBucket`)
9. [ ] Replace enum classes with string literals (e.g., `RenderMode.SURFACES` → `"SURFACES"`)
10. [ ] Update pagination: `.meta.total` → `.total`
11. [ ] Replace `api_client.rest_client` upload/download with `sdk.upload()` / `sdk.download()`
12. [ ] Replace `ApiException` with `SimScaleAPIError`
13. [ ] Remove `urllib3` retry policy setup (no longer needed)
14. [ ] Replace `table_import_api` with `sdk.table_imports` and use `sdk.upload()` for table files
15. [ ] Use `geometry_primitive` submodule (`geo.`) for geometry primitive models (`RotatableCartesianBox`, `LocalCartesianBox`, `Point`, etc.)
16. [ ] Replace direct `result.download.url` with Export API (`sdk.export.create_export()` + `sdk.download()`)
17. [ ] Replace manual polling loops with `sdk.wait_until_done()`
