from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad._root import Cad
from simscale_sdk_v1.models.collection_links import CollectionLinks
from simscale_sdk_v1.models.collection_meta import CollectionMeta


class Cads(SimScaleModel):
    links: CollectionLinks | None = Field(validation_alias="_links", serialization_alias="_links", default=None)
    meta: CollectionMeta | None = Field(validation_alias="_meta", serialization_alias="_meta", default=None)
    embedded: list[Cad] | None = Field(validation_alias="_embedded", serialization_alias="_embedded", default=None)
