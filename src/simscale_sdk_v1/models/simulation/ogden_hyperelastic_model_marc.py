from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.one_of__ogden_hyperelastic_model_marc_number_of_terms import (
    OneOf_OgdenHyperelasticModelMarcNumberOfTerms,
)


class OgdenHyperelasticModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OGDEN_MARC",
        description="Schema name: OgdenHyperelasticModelMarc",
    )
    number_of_terms: OneOf_OgdenHyperelasticModelMarcNumberOfTerms | None = Field(
        validation_alias="numberOfTerms", serialization_alias="numberOfTerms", default=None
    )
    bulk_modulus: Dimensional_Pressure | None = Field(
        validation_alias="bulkModulus", serialization_alias="bulkModulus", default=None
    )
