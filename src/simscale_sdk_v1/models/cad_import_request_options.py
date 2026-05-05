from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CadImportRequestOptions(SimScaleModel):
    """CAD import options. Please refer to https://www.simscale.com/docs/cad-preparation/#cad-upload-options for a detailed description of the options."""

    facet_split: bool = Field(
        validation_alias="facetSplit",
        serialization_alias="facetSplit",
        default=False,
        description="_Facet Split_ tries to split the faceted parts of a CAD model. This means it can create new faces from original faces. In this case it's not possible to use the original faces to make assignments.",
    )
    sewing: bool = Field(
        default=False,
        description="_Automatic Sewing_ is sewing faces or sheet bodies together. This means that it can create one new face from two (or more) original faces, as well as one solid body from two (or more) original sheet bodies. In this case, if the entities have the same ID, it will be inherited by the newly created entity. However if the original entities do not share the same ID, only one of these will be mapped to the new entity. This might not be desirable if one would like to make assignments on the original entities and not on the new (sewn) entities.",
    )
    improve: bool = Field(
        default=True,
        description="This option tries to improve the topology (e.g. edges, vertices) and geometry of the model by adjusting tolerances, simplifying entities, etc. As this option should improve CAD operations and data handling for all downstream applications it is recommended to use it on import. For very complex models it can take a considerable amount of time though, therefore you can also opt-out and reconsider in case you face issues in geometry handling or meshing.",
    )
    optimize_for_lbm_solver: bool = Field(
        validation_alias="optimizeForLBMSolver",
        serialization_alias="optimizeForLBMSolver",
        default=False,
        description="This option allows you to import a *.stl file that is optimized for the Incompressible LBM and Wind Comfort analysis types. It leaves out complex import steps like sewing and cleanup that are not required by the LBM solver and therefore also allows to import big and complex models fast.",
    )
