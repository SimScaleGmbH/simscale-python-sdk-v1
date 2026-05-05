from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.elasticity_marc import ElasticityMarc
from simscale_sdk_v1.models.simulation.plasticity_marc import PlasticityMarc


class ElastoplasticMarcMaterialBehavior(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ELASTOPLASTIC_MARC",
        description="Schema name: ElastoplasticMarcMaterialBehavior",
    )
    elasticity: ElasticityMarc | None = Field(default=None)
    plasticity: PlasticityMarc | None = Field(default=None)
