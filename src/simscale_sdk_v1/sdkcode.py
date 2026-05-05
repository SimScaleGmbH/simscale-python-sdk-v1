"""Generate Python SDK v1 code from a simulation/meshing spec.

This module ships with the SDK and can be used as a library or CLI:

    # CLI:
    python -m simscale_sdk_v1.sdkcode --project PID --simulation SID
    python -m simscale_sdk_v1.sdkcode --project PID --simulation SID --simulation-run RID
    python -m simscale_sdk_v1.sdkcode --project PID --mesh-operation MID

    # Library:
    from simscale_sdk_v1.sdkcode import generate_sdk_code
    code = generate_sdk_code(project_id="...", simulation_id="...")
    code = generate_sdk_code(project_id="...", simulation_id="...", simulation_run_id="...")

Uses the same SIMSCALE_API_KEY / SIMSCALE_API_URL environment variables as the SDK.
"""

from __future__ import annotations

import argparse
import json

from simscale_sdk_v1 import SimScaleSDK
from simscale_sdk_v1._base import SimScaleModel

_INDENT = "    "

_NAMESPACE_ALIASES = {
    "simulation": "sim",
    "meshing": "mesh",
    "material": "mat",
    "cad": "cad",
    "geometry_primitive": "geo",
    "parametric": "param",
    "postprocessing": "pp",
    "reporting": "rpt",
}


def _get_namespace(cls: type) -> str | None:
    """e.g. 'simscale_sdk_v1.models.simulation.incompressible' -> 'simulation'"""
    after_models = cls.__module__.split("models.", 1)[1]
    return after_models.split(".")[0] if "." in after_models else None


def _qualified_name(cls: type) -> str:
    """Return the namespace-prefixed class name, e.g. 'sim.Incompressible' or 'models.Project'."""
    ns = _get_namespace(cls)
    alias = _NAMESPACE_ALIASES.get(ns, ns) if ns else "models"
    return f"{alias}.{cls.__name__}"


# ---------------------------------------------------------------------------
# Code emitter — recursively convert model objects to Python source code
# ---------------------------------------------------------------------------

_Imports = dict[str, type]


def _emit(value: object, indent_level: int) -> tuple[str, _Imports]:
    """Emit any value as Python source code. Returns (code, imports)."""
    if isinstance(value, SimScaleModel):
        return _emit_model(value, indent_level)
    if isinstance(value, list):
        return _emit_list(value, indent_level)
    if isinstance(value, dict):
        return _emit_dict(value, indent_level)
    if isinstance(value, bool):
        return ("True" if value else "False"), {}
    if isinstance(value, str):
        return json.dumps(value), {}
    if value is None:
        return "None", {}
    return str(value), {}


def _emit_model(obj: object, indent_level: int) -> tuple[str, _Imports]:
    """Emit a SimScaleModel instance as a constructor call."""
    cls = type(obj)
    imports: _Imports = {cls.__name__: cls}
    name = _qualified_name(cls)

    props = []
    for field_name, field_info in cls.model_fields.items():
        if field_info.validation_alias == "type" and field_info.default is not None:
            continue
        val = getattr(obj, field_name)
        if val is None or val == [] or val == {} or val == field_info.default:
            continue
        props.append((field_name, val))

    if not props:
        return f"{name}()", imports

    lines = [f"{name}("]
    for field_name, val in props:
        prefix = _INDENT * (indent_level + 1)
        val_code, val_imports = _emit(val, indent_level + 1)
        imports.update(val_imports)
        lines.append(f"{prefix}{field_name}={val_code},")
    lines.append(f"{_INDENT * indent_level})")
    return "\n".join(lines), imports


def _emit_list(items: list, indent_level: int) -> tuple[str, _Imports]:
    if not items:
        return "[]", {}
    imports: _Imports = {}
    lines = ["["]
    for item in items:
        prefix = _INDENT * (indent_level + 1)
        item_code, item_imports = _emit(item, indent_level + 1)
        imports.update(item_imports)
        lines.append(f"{prefix}{item_code},")
    lines.append(f"{_INDENT * indent_level}]")
    return "\n".join(lines), imports


def _emit_dict(data: dict, indent_level: int) -> tuple[str, _Imports]:
    if not data:
        return "{}", {}
    imports: _Imports = {}
    lines = ["{"]
    for key, val in data.items():
        prefix = _INDENT * (indent_level + 1)
        val_code, val_imports = _emit(val, indent_level + 1)
        imports.update(val_imports)
        lines.append(f"{prefix}{json.dumps(key)}: {val_code},")
    lines.append(f"{_INDENT * indent_level}}}")
    return "\n".join(lines), imports


# ---------------------------------------------------------------------------
# Import generation
# ---------------------------------------------------------------------------


def _generate_imports(imports: _Imports) -> str:
    groups: dict[str | None, list[str]] = {}
    for cls_name, cls in sorted(imports.items()):
        groups.setdefault(_get_namespace(cls), []).append(cls_name)

    lines = []
    if groups.pop(None, []):
        lines.append("from simscale_sdk_v1 import models")
    for ns in sorted(groups.keys()):
        alias = _NAMESPACE_ALIASES.get(ns, ns)
        lines.append(f"from simscale_sdk_v1.models import {ns} as {alias}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def generate_sdk_code(
    *,
    project_id: str,
    simulation_id: str | None = None,
    simulation_run_id: str | None = None,
    mesh_operation_id: str | None = None,
) -> str:
    """Generate Python SDK v1 code by fetching a spec from the SimScale API.

    Provide ``project_id`` with one of ``simulation_id`` /
    ``mesh_operation_id``. When ``simulation_run_id`` is also provided
    alongside ``simulation_id``, the run spec is fetched instead.

    Uses the same ``SIMSCALE_API_KEY`` / ``SIMSCALE_API_URL`` environment
    variables as ``SimScaleSDK``.

    Args:
        project_id: SimScale project ID.
        simulation_id: SimScale simulation ID.
        simulation_run_id: SimScale simulation run ID.
        mesh_operation_id: SimScale mesh operation ID.

    Returns:
        Python source code string.
    """
    if simulation_id and mesh_operation_id:
        raise ValueError("Cannot specify both simulation_id and mesh_operation_id")

    with SimScaleSDK() as sdk:
        if simulation_id and simulation_run_id:
            model = sdk.simulation_runs.get_simulation_run_spec(project_id, simulation_id, simulation_run_id).model
        elif simulation_id:
            model = sdk.simulations.get_simulation(project_id, simulation_id).model
        elif mesh_operation_id:
            model = sdk.mesh_operations.get_mesh_operation(project_id, mesh_operation_id).model
        else:
            raise ValueError("Either simulation_id or mesh_operation_id must be provided")

    code, imports = _emit(model, 0)
    import_lines = _generate_imports(imports)
    return "\n\n".join(filter(None, [import_lines, code])) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Python SDK v1 code from a simulation/meshing spec.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m simscale_sdk_v1.sdkcode --project PID --simulation SID
  python -m simscale_sdk_v1.sdkcode --project PID --simulation SID --simulation-run RID
  python -m simscale_sdk_v1.sdkcode --project PID --mesh-operation MID

Uses the same environment variables as the SDK:
  SIMSCALE_API_KEY   API key (required)
  SIMSCALE_API_URL   API base URL (default: https://api.simscale.com)
""",
    )

    parser.add_argument("--project", dest="project_id", required=True, help="SimScale project ID")
    parser.add_argument("--simulation", dest="simulation_id", help="SimScale simulation ID")
    parser.add_argument("--simulation-run", dest="simulation_run_id", help="SimScale simulation run ID")
    parser.add_argument("--mesh-operation", dest="mesh_operation_id", help="SimScale mesh operation ID")

    args = parser.parse_args()

    if not args.simulation_id and not args.mesh_operation_id:
        parser.error("--simulation or --mesh-operation is required")
    if args.simulation_id and args.mesh_operation_id:
        parser.error("--simulation and --mesh-operation are mutually exclusive")

    try:
        code = generate_sdk_code(
            project_id=args.project_id,
            simulation_id=args.simulation_id,
            simulation_run_id=args.simulation_run_id,
            mesh_operation_id=args.mesh_operation_id,
        )
    except Exception as e:
        parser.exit(1, f"Error: {e}\n")
    print(code)


if __name__ == "__main__":
    main()
