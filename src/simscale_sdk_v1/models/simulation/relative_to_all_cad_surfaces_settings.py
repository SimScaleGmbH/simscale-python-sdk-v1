from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelativeToAllCadSurfacesSettings(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE_TO_ALL_CAD_SURFACES",
        description="Schema name: RelativeToAllCadSurfacesSettings",
    )
    minimum_cell_size: float | None = Field(
        validation_alias="minimumCellSize",
        serialization_alias="minimumCellSize",
        default=0.0007,
        description="This parameter specifies the minimum size for all cells of the mesh relative to the diagonal of the CAD model. A higher value leads to a coarser mesh. Our recommendation is to start with the default value and if necessary, gradually lower the parameter until a desired mesh fineness is obtained.",
    )
    maximum_cell_size: float | None = Field(
        validation_alias="maximumCellSize",
        serialization_alias="maximumCellSize",
        default=0.02,
        description="This parameter specifies the maximum size for all cells of the mesh relative to the diagonal of the CAD model. A lower value leads to a finer mesh. Our recommendation is to start with the default value and if necessary, gradually lower the parameter until a desired mesh fineness is obtained.",
    )
    cell_size_on_surfaces: float | None = Field(
        validation_alias="cellSizeOnSurfaces",
        serialization_alias="cellSizeOnSurfaces",
        default=0.01,
        description="This parameter specifies the size of cells close to the surfaces relative to the diagonal of the CAD model. A higher value leads to a coarser mesh. Our recommendation is to start with the default value and if necessary, gradually lower the parameter until a desired mesh fineness is obtained.",
    )
