from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.elastoplastic_network import ElastoplasticNetwork
from simscale_sdk_v1.models.simulation.primary_network import PrimaryNetwork
from simscale_sdk_v1.models.simulation.viscoelastic_network import ViscoelasticNetwork


class ViscoplasticMarcMaterialBehavior(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VISCOPLASTIC_MARC",
        description="Schema name: ViscoplasticMarcMaterialBehavior",
    )
    primary_network: PrimaryNetwork | None = Field(
        validation_alias="primaryNetwork", serialization_alias="primaryNetwork", default=None
    )
    viscoelastic_network: ViscoelasticNetwork | None = Field(
        validation_alias="viscoelasticNetwork", serialization_alias="viscoelasticNetwork", default=None
    )
    elastoplastic_network: ElastoplasticNetwork | None = Field(
        validation_alias="elastoplasticNetwork", serialization_alias="elastoplasticNetwork", default=None
    )
