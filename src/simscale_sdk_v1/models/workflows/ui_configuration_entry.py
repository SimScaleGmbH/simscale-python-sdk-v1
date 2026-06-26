from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.compound_field_custom_ui_configuration_entry import (
    CompoundFieldCustomUiConfigurationEntry,
)
from simscale_sdk_v1.models.workflows.compound_field_title_ui_configuration_entry import (
    CompoundFieldTitleUiConfigurationEntry,
)
from simscale_sdk_v1.models.workflows.navigation_list_ui_configuration_entry import NavigationListUiConfigurationEntry
from simscale_sdk_v1.models.workflows.navigation_ui_configuration_entry import NavigationUiConfigurationEntry
from simscale_sdk_v1.models.workflows.plot2_d_ui_configuration_entry import Plot2DUiConfigurationEntry
from simscale_sdk_v1.models.workflows.slider_ui_configuration_entry import SliderUiConfigurationEntry
from simscale_sdk_v1.models.workflows.unknown_ui_configuration_entry import UnknownUiConfigurationEntry
from simscale_sdk_v1.models.workflows.visibility_ui_configuration_entry import VisibilityUiConfigurationEntry

_UI_CONFIGURATION_ENTRY_VARIANTS: dict[str, type] = {
    "builtin:navigation": NavigationUiConfigurationEntry,
    "builtin:navigation:list": NavigationListUiConfigurationEntry,
    "builtin:plot": Plot2DUiConfigurationEntry,
    "builtin:slider": SliderUiConfigurationEntry,
    "builtin:title": CompoundFieldTitleUiConfigurationEntry,
    "builtin:visibility": VisibilityUiConfigurationEntry,
    "custom": CompoundFieldCustomUiConfigurationEntry,
    "unknown": UnknownUiConfigurationEntry,
}

UiConfigurationEntry = Annotated[
    Union[
        NavigationUiConfigurationEntry,
        NavigationListUiConfigurationEntry,
        Plot2DUiConfigurationEntry,
        SliderUiConfigurationEntry,
        CompoundFieldTitleUiConfigurationEntry,
        VisibilityUiConfigurationEntry,
        CompoundFieldCustomUiConfigurationEntry,
        UnknownUiConfigurationEntry,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="configuration_entry_type",
            variants=_UI_CONFIGURATION_ENTRY_VARIANTS,
        )
    ),
]
