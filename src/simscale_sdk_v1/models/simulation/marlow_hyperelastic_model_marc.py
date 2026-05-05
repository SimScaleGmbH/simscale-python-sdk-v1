from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class MarlowHyperelasticModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MARLOW_MARC",
        description="Schema name: MarlowHyperelasticModelMarc",
    )
    deformation_mode: Literal["UNIAXIAL", "EQUI_BIAXIAL", "PURE_SHEAR"] | None = Field(
        validation_alias="deformationMode",
        serialization_alias="deformationMode",
        default="UNIAXIAL",
        description="Select the primary deformation mode from the experimental test data generation.Uniaxial (tension): Specifies that the provided stress-strain data was obtained from a standard tensile test where the specimen is stretched in one direction. This is the most common experimental input for characterizing basic elastomer behavior.Note: For uniaxial compression tests, the data needs to first be converted and the equi-biaxial tension option used.Equi-biaxial (tension): Indicates that the input data comes from a test where equal tensile loads were applied in two perpendicular directions. This mode is critical for accurately modeling materials that will experience significant stretching in two dimensions, such as inflatable membranes.Pure Shear: Used when the input data is derived from a planar tension test where the width of the specimen is much larger than its length, preventing lateral contraction. This data helps the solver better predict the material's response under shearing or complex combined loading.",
    )
    engineering_stress_strain_curve: DimensionalFunction_Pressure | None = Field(
        validation_alias="engineeringStressStrainCurve",
        serialization_alias="engineeringStressStrainCurve",
        default=None,
    )
    bulk_modulus: Dimensional_Pressure | None = Field(
        validation_alias="bulkModulus", serialization_alias="bulkModulus", default=None
    )
