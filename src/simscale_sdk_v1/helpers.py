"""Helper methods mixed into SimScaleSDK."""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING

from simscale_sdk_v1.client import SimScaleOperationError

if TYPE_CHECKING:
    from simscale_sdk_v1 import models


class SimScaleHelpers:
    """Mixin providing convenience methods for SimScaleSDK."""

    def wait_until_done(
        self,
        poll_fn,
        *,
        timeout=3600,
        interval=30,
        terminal_statuses=("FINISHED", "CANCELED", "FAILED", "DONE", "EXPIRED"),
        success_statuses=("FINISHED", "DONE"),
        raise_on_failure=True,
    ):
        """Poll until status reaches a terminal state.

        Raises SimScaleOperationError if the operation fails (unless raise_on_failure=False).
        Raises TimeoutError if timeout is exceeded.
        """
        start = time.monotonic()
        result = poll_fn()
        while result.status not in terminal_statuses:
            if time.monotonic() - start > timeout:
                raise TimeoutError(f"Timed out after {timeout}s (last status: {result.status})")
            time.sleep(interval)
            result = poll_fn()
        if raise_on_failure and result.status not in success_statuses:
            raise SimScaleOperationError(result)
        return result

    def get_material(self, name: str, *, group: str | None = None) -> models.MaterialResponse:
        """Look up a material by name. Uses the SimScale default library unless group is specified."""
        groups = self.materials.get_material_groups(limit=100).embedded
        if group:
            material_group = next((g for g in groups if g.name == group), None)
            if not material_group:
                available = [g.name for g in groups]
                raise ValueError(f"Material group '{group}' not found. Available: {available}")
        else:
            material_group = next(
                (g for g in groups if g.group_type == "SIMSCALE_DEFAULT"),
                None,
            )
            if not material_group:
                raise ValueError("Could not find the SimScale default material group")
        materials = self.materials.get_materials(material_group_id=material_group.material_group_id, limit=100).embedded
        material = next((m for m in materials if m.name == name), None)
        if not material:
            available = [m.name for m in materials]
            raise ValueError(f"Material '{name}' not found. Available: {available}")
        return self.materials.get_material_data(
            material_group_id=material_group.material_group_id,
            material_id=material.id,
        )

    def upload(self, filepath: str | Path) -> models.Storage:
        """Create a storage entry and upload a file. Returns the Storage object (use .storage_id)."""
        storage = self.storage.create_storage()
        self._client.upload_to_storage(storage.url, filepath)
        return storage

    def download(self, url: str, filepath: str | Path) -> None:
        """Download a file from a URL to a local path."""
        self._client.download(url, filepath)

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args) -> None:
        self.close()
