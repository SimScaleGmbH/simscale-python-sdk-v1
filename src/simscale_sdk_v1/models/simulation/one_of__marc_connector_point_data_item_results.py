from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.all_connector_point_data_results import AllConnectorPointDataResults
from simscale_sdk_v1.models.simulation.custom_connector_point_data_results import CustomConnectorPointDataResults

# All: Exports all available physical quantities associated with the connector elements for comprehensive tracking - displacements, rotations, forces and moments.Custom: Allows for the selection of specific output variables (like force or displacement) to be recorded at the connector locations.
_ONE_OF__MARC_CONNECTOR_POINT_DATA_ITEM_RESULTS_VARIANTS: dict[str, type] = {
    "ALL": AllConnectorPointDataResults,
    "CUSTOM": CustomConnectorPointDataResults,
}

OneOf_MarcConnectorPointDataItemResults = Annotated[
    Union[AllConnectorPointDataResults, CustomConnectorPointDataResults],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_CONNECTOR_POINT_DATA_ITEM_RESULTS_VARIANTS,
        )
    ),
]
