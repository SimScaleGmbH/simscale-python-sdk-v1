from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.feature_parameters import FeatureParameters


class CadFeatureRequest(SimScaleModel):
    feature: Literal[
        "close_sheet_v2",
        "create_box",
        "create_cylinder_v3",
        "delete_face_v2",
        "delete_occurrences",
        "extrude_faces",
        "facet_split_bodies",
        "fix_interferences",
        "flow_volume_create_caps",
        "flow_volume_extraction_external",
        "flow_volume_extraction_internal",
        "imprint_bodies",
        "improve_bodies",
        "intersect_bodies",
        "move_faces",
        "rotate_bodies",
        "scale_bodies",
        "simplify",
        "split_bodies",
        "subtract_bodies",
        "translate_bodies",
        "union_bodies",
        "wrap_occurrences",
    ] = Field(
        description="Available feature types: - `close_sheet_v2`: Close selected sheet bodies in order to create solid regions. - `create_box`: Create a box body from selected faces or from the given dimensions. - `create_cylinder_v3`: Create a cylindrical body from selected faces or from the given center, axis, radius and height. - `delete_face_v2`: Delete selected faces. - `delete_occurrences`: Delete selected sheet bodies or solid regions. - `extrude_faces`: Extrude selected faces for a given distance or up to a given entity. - `facet_split_bodies`: Create faces in the input sheet bodies and/or solid regions by defining edges based on the given split angle. This feature impacts only bodies with underlying triangulated geometry. - `fix_interferences`: Remove any interference between solid regions in the model. The interferences are removed by subtracting interfering parts from the larger solid region. - `flow_volume_create_caps`: Create a sheet body whose faces cover the holes defined by the given boundary faces. The operation is intended for defining the internal flow volume in the Immersed Boundary analysis. - `flow_volume_extraction_external`: Create a body that represents an external flow volume. The flow volume boundary is defined by the bounding box and the model itself. If the flow volume is disjoint, a seed face can be used to select one of the flow regions. - `flow_volume_extraction_internal`: Create a body that represents an internal flow volume. The flow spans from the seed face to the boundary faces. The boundary faces describe holes in the model that must be closed by the internal flow volume. - `imprint_bodies`: Create faces on the contact surface between two sheet bodies and/or solid regions. The shape of the new face will correspond to the profile of the part in contact. - `intersect_bodies`: Create a body by intersecting the selected sheet bodies and/or solid regions. - `move_faces`: Move selected faces for a given distance or up to a given entity. The operation modifies all adjacent faces accordingly. - `rotate_bodies`: Rotate selected sheet bodies and/or solid regions around an axis for a given angle. - `scale_bodies`: Scale selected sheet bodies and/or solid regions with a given scaling factor. - `simplify`: Replace selected sheet bodies and/or solid regions with a box or a cylinder. - `split_bodies`: Split selected sheet bodies and/or solid regions in two by a given plane. - `subtract_bodies`: Subtract selected tool sheet bodies and/or solid regions from target sheet bodies and/or solid regions. - `translate_bodies`: Translate selected sheet bodies and/or solid regions either in a given direction and for a selected distance, or up to a given entity. - `union_bodies`: Unite the selected sheet bodies and/or solid regions. The operation produces up to two resulting bodies: one sheet body and one solid body, since sheet bodies and solid bodies are merged independently. - `wrap_occurrences`: Create a solid body that wraps selected sheet bodies and/or solid regions."
    )
    parameters: FeatureParameters | None = Field(default=None)
