# SimScale Python SDK v1

The official Python SDK for the SimScale API v1. Provides strongly-typed models and a simple entry point for all API resources.

> Migrating from v0? See [MIGRATION.md](./MIGRATION.md).

## Requirements

- Python 3.10+

## Installation

```bash
pip install git+https://github.com/SimScaleGmbH/simscale-python-sdk-v1.git
```

## Quick Start

```python
from simscale_sdk_v1 import SimScaleSDK, models

sdk = SimScaleSDK()  # reads SIMSCALE_API_KEY from environment

# Create a project
project = sdk.projects.create_project(
    models.Project(
        name="My Project",
        description="Created via SDK",
        measurement_system="SI",
    )
)
print(f"Created project: {project.project_id}")
```

## Configuration

By default, `SimScaleSDK()` reads configuration from environment variables:

| Environment Variable | Description |
|---------------------|-------------|
| `SIMSCALE_API_KEY` | Your SimScale API key (required) |
| `SIMSCALE_API_URL` | API base URL (optional, defaults to `https://api.simscale.com`) |

You can also pass them explicitly:

```python
import os
sdk = SimScaleSDK(api_key=os.getenv("SIMSCALE_API_KEY"))
```

### Setting Environment Variables

```sh
export SIMSCALE_API_KEY="your-api-key"
# Optional: override API URL (defaults to https://api.simscale.com)
# export SIMSCALE_API_URL="https://api.simscale.com"
```

On Windows, use `set SIMSCALE_API_KEY=your-api-key` (CMD) or `$env:SIMSCALE_API_KEY="your-api-key"` (PowerShell).

## SDK Structure

All API resources are accessed as attributes on the `SimScaleSDK` object:

```python
sdk.projects            # Create, get, update, copy projects
sdk.cad_imports         # Import CAD files
sdk.cads                # Query CAD topology and entities
sdk.mesh_operations     # Create and run mesh operations
sdk.meshes              # Retrieve mesh information
sdk.simulations         # Simulation setup and configuration
sdk.simulation_runs     # Start, monitor, and retrieve simulation runs
sdk.materials           # Browse and retrieve materials
sdk.export              # Export simulation results
sdk.reports             # Create and download reports
sdk.postprocessing      # Post-processing operations
sdk.storage             # Create storage for file uploads
sdk.table_imports       # Import table data
```

### Models

Model classes are organized under `simscale_sdk_v1.models`, with domain-specific models in submodules:

```python
from simscale_sdk_v1 import models

# Core API models are at the top level
project = models.Project(name="My Project", description="...", measurement_system="SI")

# Domain models are in submodules
from simscale_sdk_v1.models import simulation as sim, meshing as mesh

model = sim.Incompressible(...)
mesh_model = mesh.SimmetrixMeshingFluid(...)
```

Available submodules: `cad`, `meshing`, `simulation`, `material`, `reporting`, `postprocessing`, `geometry_primitive`, `parametric`.

### Pagination

Methods that return lists return a `PaginatedResponse` with one page of results:

```python
result = sdk.projects.get_projects(limit=10, page=1)
print(f"Total projects: {result.total}")  # total across all pages
for project in result.embedded:           # items on this page
    print(project.name)
```

To iterate all pages, increment `page` until all items are retrieved.

### Error Handling

API errors raise `SimScaleAPIError`. Failed long-running operations (mesh, simulation run, etc.) raise `SimScaleOperationError`:

```python
from simscale_sdk_v1 import SimScaleAPIError, SimScaleOperationError

try:
    sdk.projects.get_project("nonexistent-id")
except SimScaleAPIError as e:
    print(f"Status: {e.status_code}")
    print(f"Body: {e.body}")
```

`SimScaleOperationError` is raised automatically by `sdk.wait_until_done()` when an operation finishes with a failure status.

## Helper Methods

### upload

Create a storage entry and upload a file in one call:

```python
storage = sdk.upload("model.stl")
storage_id = storage.storage_id  # use in CadImportRequest
```

### download

Download a file from a URL to a local path:

```python
sdk.download(export.url, "result.csv")
```

### wait_until_done

Generic polling helper that waits for an operation to complete. Raises `SimScaleOperationError` on failure:

```python
mesh_op = sdk.wait_until_done(
    lambda: sdk.mesh_operations.get_mesh_operation(project_id, mesh_op_id),
    timeout=3600, interval=30,
)
```

Parameters:
- `poll_fn` — function that fetches the current state (must return an object with a `.status` attribute)
- `timeout` — maximum time to wait in seconds (default: 3600)
- `interval` — polling interval in seconds (default: 30)
- `raise_on_failure` — raise `SimScaleOperationError` on failure (default: True)

### get_material

Look up a material by name from the SimScale material library:

```python
water_data = sdk.get_material("Water")
custom_mat = sdk.get_material("Steel", group="My Custom Group")
```

## Examples

The `examples/` folder contains complete, runnable scripts:

| Example | Description |
|---------|-------------|
| `incompressible_example.py` | End-to-end CFD workflow: project creation, CAD upload/import, simulation setup, meshing, run execution, result export, and report generation |
| `incompressible_lbm_example.py` | Incompressible LBM (Pacefish): table imports (CSV inlet profiles, probe points), flow domain boundaries, geometry primitives, mesh refinement regions, transient/statistical/snapshot result controls, forces/moments tracking, and screenshot report |
| `pedestrian_wind_comfort_example.py` | Pedestrian Wind Comfort (PWC): wind rose data, geographical location, region of interest, comfort surfaces, Wind API integration, and additional wind data for reusing directional results |
| `folders_and_spaces_example.py` | Space and folder management: creation, listing, moving, and deletion |

### Running Examples

```bash
cd examples
python incompressible_example.py
```

## SDK Code Generator

The SDK includes a tool that generates Python SDK code from existing simulation or meshing specs. This is useful for bootstrapping SDK scripts from simulations set up in the SimScale workbench.

### CLI Usage

```bash
# Fetch a simulation spec from the API and generate SDK code:
python -m simscale_sdk_v1.sdkcode --project PROJECT_ID --simulation SIMULATION_ID

# Fetch a simulation run spec:
python -m simscale_sdk_v1.sdkcode --project PROJECT_ID --simulation SIMULATION_ID --simulation-run RUN_ID

# Fetch a mesh operation spec:
python -m simscale_sdk_v1.sdkcode --project PROJECT_ID --mesh-operation MESH_OPERATION_ID
```

The tool uses the same `SIMSCALE_API_KEY` and `SIMSCALE_API_URL` environment variables as the SDK.

### Library Usage

```python
from simscale_sdk_v1.sdkcode import generate_sdk_code

# Fetch from the API and generate code:
code = generate_sdk_code(project_id="...", simulation_id="...")

# Fetch from a simulation run:
code = generate_sdk_code(project_id="...", simulation_id="...", simulation_run_id="...")

print(code)
```

The generated code uses the same namespace aliases as the examples (`sim.`, `mesh.`, `geo.`, etc.) and includes the necessary import statements.

