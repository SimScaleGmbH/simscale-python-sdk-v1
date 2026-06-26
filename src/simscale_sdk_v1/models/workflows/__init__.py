"""Generated Workflows models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.workflows.abstract_compound_field import AbstractCompoundField
    from simscale_sdk_v1.models.workflows.abstract_compound_value import AbstractCompoundValue
    from simscale_sdk_v1.models.workflows.abstract_data_definition import AbstractDataDefinition
    from simscale_sdk_v1.models.workflows.abstract_operation_definition import AbstractOperationDefinition
    from simscale_sdk_v1.models.workflows.as_boolean_value import AsBooleanValue
    from simscale_sdk_v1.models.workflows.as_dimensional_scalar_value import AsDimensionalScalarValue
    from simscale_sdk_v1.models.workflows.as_dimensional_vector_value import AsDimensionalVectorValue
    from simscale_sdk_v1.models.workflows.as_entity_assignment_list_value import AsEntityAssignmentListValue
    from simscale_sdk_v1.models.workflows.as_entity_assignment_value import AsEntityAssignmentValue
    from simscale_sdk_v1.models.workflows.as_enum_value import AsEnumValue
    from simscale_sdk_v1.models.workflows.as_integer_value import AsIntegerValue
    from simscale_sdk_v1.models.workflows.as_measurement_unit_value import AsMeasurementUnitValue
    from simscale_sdk_v1.models.workflows.as_real_value import AsRealValue
    from simscale_sdk_v1.models.workflows.as_string_value import AsStringValue
    from simscale_sdk_v1.models.workflows.as_value_list import AsValueList
    from simscale_sdk_v1.models.workflows.atomic_field import AtomicField
    from simscale_sdk_v1.models.workflows.atomic_operation_definition import AtomicOperationDefinition
    from simscale_sdk_v1.models.workflows.boolean_comparison_equal import BooleanComparisonEqual
    from simscale_sdk_v1.models.workflows.boolean_comparison_not_equal import BooleanComparisonNotEqual
    from simscale_sdk_v1.models.workflows.boolean_constant import BooleanConstant
    from simscale_sdk_v1.models.workflows.boolean_expression_select import BooleanExpressionSelect
    from simscale_sdk_v1.models.workflows.boolean_field import BooleanField
    from simscale_sdk_v1.models.workflows.boolean_operation_and import BooleanOperationAnd
    from simscale_sdk_v1.models.workflows.boolean_operation_not import BooleanOperationNot
    from simscale_sdk_v1.models.workflows.boolean_operation_or import BooleanOperationOr
    from simscale_sdk_v1.models.workflows.boolean_operation_xor import BooleanOperationXor
    from simscale_sdk_v1.models.workflows.boolean_reference import BooleanReference
    from simscale_sdk_v1.models.workflows.boolean_to_string_value_conversion import BooleanToStringValueConversion
    from simscale_sdk_v1.models.workflows.boolean_value import BooleanValue
    from simscale_sdk_v1.models.workflows.breakpoint import Breakpoint
    from simscale_sdk_v1.models.workflows.compound_comparison_equal import CompoundComparisonEqual
    from simscale_sdk_v1.models.workflows.compound_expression_select import CompoundExpressionSelect
    from simscale_sdk_v1.models.workflows.compound_field import CompoundField
    from simscale_sdk_v1.models.workflows.compound_field_custom_ui_configuration_entry import (
        CompoundFieldCustomUiConfigurationEntry,
    )
    from simscale_sdk_v1.models.workflows.compound_field_title_ui_configuration_entry import (
        CompoundFieldTitleUiConfigurationEntry,
    )
    from simscale_sdk_v1.models.workflows.compound_map_entities import CompoundMapEntities
    from simscale_sdk_v1.models.workflows.compound_value import CompoundValue
    from simscale_sdk_v1.models.workflows.config_value_reference import ConfigValueReference
    from simscale_sdk_v1.models.workflows.constant_value_list import ConstantValueList
    from simscale_sdk_v1.models.workflows.data_mapping_entry import DataMappingEntry
    from simscale_sdk_v1.models.workflows.data_presence_reference import DataPresenceReference
    from simscale_sdk_v1.models.workflows.data_reference import DataReference
    from simscale_sdk_v1.models.workflows.data_value_reference import DataValueReference
    from simscale_sdk_v1.models.workflows.dimensional_field import DimensionalField
    from simscale_sdk_v1.models.workflows.dimensional_profile_object_dimension import DimensionalProfileObjectDimension
    from simscale_sdk_v1.models.workflows.dimensional_profiles_object_dimension import (
        DimensionalProfilesObjectDimension,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar import DimensionalScalar
    from simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_greater_than import (
        DimensionalScalarComparisonGreaterThan,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_greater_than_or_equal import (
        DimensionalScalarComparisonGreaterThanOrEqual,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_less_than import (
        DimensionalScalarComparisonLessThan,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_less_than_or_equal import (
        DimensionalScalarComparisonLessThanOrEqual,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar_constant import DimensionalScalarConstant
    from simscale_sdk_v1.models.workflows.dimensional_scalar_expression_select import DimensionalScalarExpressionSelect
    from simscale_sdk_v1.models.workflows.dimensional_scalar_from_dimensional_vector_component import (
        DimensionalScalarFromDimensionalVectorComponent,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar_function_pow import DimensionalScalarFunctionPow
    from simscale_sdk_v1.models.workflows.dimensional_scalar_object import DimensionalScalarObject
    from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_div import DimensionalScalarOperationDiv
    from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_minus import DimensionalScalarOperationMinus
    from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_plus import DimensionalScalarOperationPlus
    from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_times import DimensionalScalarOperationTimes
    from simscale_sdk_v1.models.workflows.dimensional_scalar_reference import DimensionalScalarReference
    from simscale_sdk_v1.models.workflows.dimensional_scalar_to_real_value_conversion import (
        DimensionalScalarToRealValueConversion,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar_to_string_value_conversion import (
        DimensionalScalarToStringValueConversion,
    )
    from simscale_sdk_v1.models.workflows.dimensional_scalar_value import DimensionalScalarValue
    from simscale_sdk_v1.models.workflows.dimensional_vector import DimensionalVector
    from simscale_sdk_v1.models.workflows.dimensional_vector_constant import DimensionalVectorConstant
    from simscale_sdk_v1.models.workflows.dimensional_vector_expression_select import DimensionalVectorExpressionSelect
    from simscale_sdk_v1.models.workflows.dimensional_vector_from_components import DimensionalVectorFromComponents
    from simscale_sdk_v1.models.workflows.dimensional_vector_function_mag import DimensionalVectorFunctionMag
    from simscale_sdk_v1.models.workflows.dimensional_vector_function_norm import DimensionalVectorFunctionNorm
    from simscale_sdk_v1.models.workflows.dimensional_vector_object import DimensionalVectorObject
    from simscale_sdk_v1.models.workflows.dimensional_vector_operation_div import DimensionalVectorOperationDiv
    from simscale_sdk_v1.models.workflows.dimensional_vector_operation_minus import DimensionalVectorOperationMinus
    from simscale_sdk_v1.models.workflows.dimensional_vector_operation_plus import DimensionalVectorOperationPlus
    from simscale_sdk_v1.models.workflows.dimensional_vector_operation_times import DimensionalVectorOperationTimes
    from simscale_sdk_v1.models.workflows.dimensional_vector_reference import DimensionalVectorReference
    from simscale_sdk_v1.models.workflows.dimensional_vector_to_string_value_conversion import (
        DimensionalVectorToStringValueConversion,
    )
    from simscale_sdk_v1.models.workflows.dimensional_vector_value import DimensionalVectorValue
    from simscale_sdk_v1.models.workflows.entity_assignment import EntityAssignment
    from simscale_sdk_v1.models.workflows.entity_assignment_constant import EntityAssignmentConstant
    from simscale_sdk_v1.models.workflows.entity_assignment_field import EntityAssignmentField
    from simscale_sdk_v1.models.workflows.entity_assignment_function_is_empty import EntityAssignmentFunctionIsEmpty
    from simscale_sdk_v1.models.workflows.entity_assignment_list import EntityAssignmentList
    from simscale_sdk_v1.models.workflows.entity_assignment_list_constant import EntityAssignmentListConstant
    from simscale_sdk_v1.models.workflows.entity_assignment_list_from_components import (
        EntityAssignmentListFromComponents,
    )
    from simscale_sdk_v1.models.workflows.entity_assignment_list_function_count_entities import (
        EntityAssignmentListFunctionCountEntities,
    )
    from simscale_sdk_v1.models.workflows.entity_assignment_list_function_is_empty import (
        EntityAssignmentListFunctionIsEmpty,
    )
    from simscale_sdk_v1.models.workflows.entity_assignment_list_intersect import EntityAssignmentListIntersect
    from simscale_sdk_v1.models.workflows.entity_assignment_list_map_entities import EntityAssignmentListMapEntities
    from simscale_sdk_v1.models.workflows.entity_assignment_list_reference import EntityAssignmentListReference
    from simscale_sdk_v1.models.workflows.entity_assignment_list_to_markdown_link_value_conversion import (
        EntityAssignmentListToMarkdownLinkValueConversion,
    )
    from simscale_sdk_v1.models.workflows.entity_assignment_list_value import EntityAssignmentListValue
    from simscale_sdk_v1.models.workflows.entity_assignment_map_entities import EntityAssignmentMapEntities
    from simscale_sdk_v1.models.workflows.entity_assignment_reference import EntityAssignmentReference
    from simscale_sdk_v1.models.workflows.entity_assignment_source import EntityAssignmentSource
    from simscale_sdk_v1.models.workflows.entity_assignment_to_entity_assignment_list_value_conversion import (
        EntityAssignmentToEntityAssignmentListValueConversion,
    )
    from simscale_sdk_v1.models.workflows.entity_assignment_to_markdown_link_value_conversion import (
        EntityAssignmentToMarkdownLinkValueConversion,
    )
    from simscale_sdk_v1.models.workflows.entity_assignment_to_string_value_conversion import (
        EntityAssignmentToStringValueConversion,
    )
    from simscale_sdk_v1.models.workflows.entity_assignment_value import EntityAssignmentValue
    from simscale_sdk_v1.models.workflows.enum_comparison_equal import EnumComparisonEqual
    from simscale_sdk_v1.models.workflows.enum_comparison_not_equal import EnumComparisonNotEqual
    from simscale_sdk_v1.models.workflows.enum_constant import EnumConstant
    from simscale_sdk_v1.models.workflows.enum_expression_select import EnumExpressionSelect
    from simscale_sdk_v1.models.workflows.enum_field import EnumField
    from simscale_sdk_v1.models.workflows.enum_function_one_of import EnumFunctionOneOf
    from simscale_sdk_v1.models.workflows.enum_reference import EnumReference
    from simscale_sdk_v1.models.workflows.enum_to_string_value_conversion import EnumToStringValueConversion
    from simscale_sdk_v1.models.workflows.enum_value import EnumValue
    from simscale_sdk_v1.models.workflows.enum_value_doc import EnumValueDoc
    from simscale_sdk_v1.models.workflows.enum_value_label import EnumValueLabel
    from simscale_sdk_v1.models.workflows.general_metadata_value_reference import GeneralMetadataValueReference
    from simscale_sdk_v1.models.workflows.gpu_scaling_estimation_value_model import GpuScalingEstimationValueModel
    from simscale_sdk_v1.models.workflows.inline_operation_definition import InlineOperationDefinition
    from simscale_sdk_v1.models.workflows.input_data_definition import InputDataDefinition
    from simscale_sdk_v1.models.workflows.integer_comparison_equal import IntegerComparisonEqual
    from simscale_sdk_v1.models.workflows.integer_comparison_greater_than import IntegerComparisonGreaterThan
    from simscale_sdk_v1.models.workflows.integer_comparison_greater_than_or_equal import (
        IntegerComparisonGreaterThanOrEqual,
    )
    from simscale_sdk_v1.models.workflows.integer_comparison_less_than import IntegerComparisonLessThan
    from simscale_sdk_v1.models.workflows.integer_comparison_less_than_or_equal import IntegerComparisonLessThanOrEqual
    from simscale_sdk_v1.models.workflows.integer_comparison_not_equal import IntegerComparisonNotEqual
    from simscale_sdk_v1.models.workflows.integer_constant import IntegerConstant
    from simscale_sdk_v1.models.workflows.integer_expression_select import IntegerExpressionSelect
    from simscale_sdk_v1.models.workflows.integer_field import IntegerField
    from simscale_sdk_v1.models.workflows.integer_function_abs import IntegerFunctionAbs
    from simscale_sdk_v1.models.workflows.integer_function_max import IntegerFunctionMax
    from simscale_sdk_v1.models.workflows.integer_function_min import IntegerFunctionMin
    from simscale_sdk_v1.models.workflows.integer_operation_div import IntegerOperationDiv
    from simscale_sdk_v1.models.workflows.integer_operation_minus import IntegerOperationMinus
    from simscale_sdk_v1.models.workflows.integer_operation_plus import IntegerOperationPlus
    from simscale_sdk_v1.models.workflows.integer_operation_rem import IntegerOperationRem
    from simscale_sdk_v1.models.workflows.integer_operation_times import IntegerOperationTimes
    from simscale_sdk_v1.models.workflows.integer_reference import IntegerReference
    from simscale_sdk_v1.models.workflows.integer_sequence_generator import IntegerSequenceGenerator
    from simscale_sdk_v1.models.workflows.integer_to_dimensional_scalar_value_conversion import (
        IntegerToDimensionalScalarValueConversion,
    )
    from simscale_sdk_v1.models.workflows.integer_to_real_value_conversion import IntegerToRealValueConversion
    from simscale_sdk_v1.models.workflows.integer_to_string_value_conversion import IntegerToStringValueConversion
    from simscale_sdk_v1.models.workflows.integer_value import IntegerValue
    from simscale_sdk_v1.models.workflows.intermediate_data_definition import IntermediateDataDefinition
    from simscale_sdk_v1.models.workflows.iterator_reference import IteratorReference
    from simscale_sdk_v1.models.workflows.json_node import JsonNode
    from simscale_sdk_v1.models.workflows.measurement_unit_comparison_equal import MeasurementUnitComparisonEqual
    from simscale_sdk_v1.models.workflows.measurement_unit_comparison_not_equal import MeasurementUnitComparisonNotEqual
    from simscale_sdk_v1.models.workflows.measurement_unit_constant import MeasurementUnitConstant
    from simscale_sdk_v1.models.workflows.measurement_unit_expression_select import MeasurementUnitExpressionSelect
    from simscale_sdk_v1.models.workflows.measurement_unit_field import MeasurementUnitField
    from simscale_sdk_v1.models.workflows.measurement_unit_function_pow import MeasurementUnitFunctionPow
    from simscale_sdk_v1.models.workflows.measurement_unit_operation_div import MeasurementUnitOperationDiv
    from simscale_sdk_v1.models.workflows.measurement_unit_operation_times import MeasurementUnitOperationTimes
    from simscale_sdk_v1.models.workflows.measurement_unit_reference import MeasurementUnitReference
    from simscale_sdk_v1.models.workflows.measurement_unit_value import MeasurementUnitValue
    from simscale_sdk_v1.models.workflows.metadata_value_reference import MetadataValueReference
    from simscale_sdk_v1.models.workflows.method_operation_definition import MethodOperationDefinition
    from simscale_sdk_v1.models.workflows.method_resource_estimation_value_model import (
        MethodResourceEstimationValueModel,
    )
    from simscale_sdk_v1.models.workflows.navigation_list_ui_configuration_entry import (
        NavigationListUiConfigurationEntry,
    )
    from simscale_sdk_v1.models.workflows.navigation_ui_configuration_entry import NavigationUiConfigurationEntry
    from simscale_sdk_v1.models.workflows.nested_schema_field import NestedSchemaField
    from simscale_sdk_v1.models.workflows.nested_workflow_operation_definition import NestedWorkflowOperationDefinition
    from simscale_sdk_v1.models.workflows.one_gpu_estimation_value_model import OneGpuEstimationValueModel
    from simscale_sdk_v1.models.workflows.one_processor_estimation_value_model import OneProcessorEstimationValueModel
    from simscale_sdk_v1.models.workflows.operation_group_definition import OperationGroupDefinition
    from simscale_sdk_v1.models.workflows.operation_group_with_condition_definition import (
        OperationGroupWithConditionDefinition,
    )
    from simscale_sdk_v1.models.workflows.operation_group_with_parameter_definition import (
        OperationGroupWithParameterDefinition,
    )
    from simscale_sdk_v1.models.workflows.output_data_definition import OutputDataDefinition
    from simscale_sdk_v1.models.workflows.pair_boolean_value_abstract_compound_value import (
        PairBooleanValueAbstractCompoundValue,
    )
    from simscale_sdk_v1.models.workflows.pair_boolean_value_boolean_value import PairBooleanValueBooleanValue
    from simscale_sdk_v1.models.workflows.pair_boolean_value_dimensional_scalar_value import (
        PairBooleanValueDimensionalScalarValue,
    )
    from simscale_sdk_v1.models.workflows.pair_boolean_value_dimensional_vector_value import (
        PairBooleanValueDimensionalVectorValue,
    )
    from simscale_sdk_v1.models.workflows.pair_boolean_value_enum_value import PairBooleanValueEnumValue
    from simscale_sdk_v1.models.workflows.pair_boolean_value_integer_value import PairBooleanValueIntegerValue
    from simscale_sdk_v1.models.workflows.pair_boolean_value_measurement_unit_value import (
        PairBooleanValueMeasurementUnitValue,
    )
    from simscale_sdk_v1.models.workflows.pair_boolean_value_real_value import PairBooleanValueRealValue
    from simscale_sdk_v1.models.workflows.pair_boolean_value_string_value import PairBooleanValueStringValue
    from simscale_sdk_v1.models.workflows.pair_boolean_value_value_list_value import PairBooleanValueValueListValue
    from simscale_sdk_v1.models.workflows.parameter_value_combination import ParameterValueCombination
    from simscale_sdk_v1.models.workflows.plot2_d_ui_configuration_entry import Plot2DUiConfigurationEntry
    from simscale_sdk_v1.models.workflows.polymorphic_compound_type_check import PolymorphicCompoundTypeCheck
    from simscale_sdk_v1.models.workflows.real_comparison_equal import RealComparisonEqual
    from simscale_sdk_v1.models.workflows.real_comparison_greater_than import RealComparisonGreaterThan
    from simscale_sdk_v1.models.workflows.real_comparison_greater_than_or_equal import RealComparisonGreaterThanOrEqual
    from simscale_sdk_v1.models.workflows.real_comparison_less_than import RealComparisonLessThan
    from simscale_sdk_v1.models.workflows.real_comparison_less_than_or_equal import RealComparisonLessThanOrEqual
    from simscale_sdk_v1.models.workflows.real_comparison_not_equal import RealComparisonNotEqual
    from simscale_sdk_v1.models.workflows.real_constant import RealConstant
    from simscale_sdk_v1.models.workflows.real_expression_select import RealExpressionSelect
    from simscale_sdk_v1.models.workflows.real_field import RealField
    from simscale_sdk_v1.models.workflows.real_function_a_cos import RealFunctionACos
    from simscale_sdk_v1.models.workflows.real_function_a_sin import RealFunctionASin
    from simscale_sdk_v1.models.workflows.real_function_a_tan import RealFunctionATan
    from simscale_sdk_v1.models.workflows.real_function_a_tan2 import RealFunctionATan2
    from simscale_sdk_v1.models.workflows.real_function_abs import RealFunctionAbs
    from simscale_sdk_v1.models.workflows.real_function_cbrt import RealFunctionCbrt
    from simscale_sdk_v1.models.workflows.real_function_cos import RealFunctionCos
    from simscale_sdk_v1.models.workflows.real_function_exp import RealFunctionExp
    from simscale_sdk_v1.models.workflows.real_function_log import RealFunctionLog
    from simscale_sdk_v1.models.workflows.real_function_log10 import RealFunctionLog10
    from simscale_sdk_v1.models.workflows.real_function_max import RealFunctionMax
    from simscale_sdk_v1.models.workflows.real_function_min import RealFunctionMin
    from simscale_sdk_v1.models.workflows.real_function_pow import RealFunctionPow
    from simscale_sdk_v1.models.workflows.real_function_sin import RealFunctionSin
    from simscale_sdk_v1.models.workflows.real_function_sqrt import RealFunctionSqrt
    from simscale_sdk_v1.models.workflows.real_function_tan import RealFunctionTan
    from simscale_sdk_v1.models.workflows.real_operation_div import RealOperationDiv
    from simscale_sdk_v1.models.workflows.real_operation_minus import RealOperationMinus
    from simscale_sdk_v1.models.workflows.real_operation_plus import RealOperationPlus
    from simscale_sdk_v1.models.workflows.real_operation_times import RealOperationTimes
    from simscale_sdk_v1.models.workflows.real_reference import RealReference
    from simscale_sdk_v1.models.workflows.real_sequence_generator import RealSequenceGenerator
    from simscale_sdk_v1.models.workflows.real_to_dimensional_scalar_value_conversion import (
        RealToDimensionalScalarValueConversion,
    )
    from simscale_sdk_v1.models.workflows.real_to_integer_conversion import RealToIntegerConversion
    from simscale_sdk_v1.models.workflows.real_to_string_value_conversion import RealToStringValueConversion
    from simscale_sdk_v1.models.workflows.real_value import RealValue
    from simscale_sdk_v1.models.workflows.reference_value_list import ReferenceValueList
    from simscale_sdk_v1.models.workflows.scaling_estimation_value_model import ScalingEstimationValueModel
    from simscale_sdk_v1.models.workflows.schema_definition import SchemaDefinition
    from simscale_sdk_v1.models.workflows.schema_element import SchemaElement
    from simscale_sdk_v1.models.workflows.serializable_data_map import SerializableDataMap
    from simscale_sdk_v1.models.workflows.slider_ui_configuration_entry import SliderUiConfigurationEntry
    from simscale_sdk_v1.models.workflows.string_comparison_equal import StringComparisonEqual
    from simscale_sdk_v1.models.workflows.string_comparison_not_equal import StringComparisonNotEqual
    from simscale_sdk_v1.models.workflows.string_constant import StringConstant
    from simscale_sdk_v1.models.workflows.string_contains_function import StringContainsFunction
    from simscale_sdk_v1.models.workflows.string_ends_with_function import StringEndsWithFunction
    from simscale_sdk_v1.models.workflows.string_expression_select import StringExpressionSelect
    from simscale_sdk_v1.models.workflows.string_field import StringField
    from simscale_sdk_v1.models.workflows.string_length_function import StringLengthFunction
    from simscale_sdk_v1.models.workflows.string_lower_case_function import StringLowerCaseFunction
    from simscale_sdk_v1.models.workflows.string_operation_plus import StringOperationPlus
    from simscale_sdk_v1.models.workflows.string_reference import StringReference
    from simscale_sdk_v1.models.workflows.string_starts_with_function import StringStartsWithFunction
    from simscale_sdk_v1.models.workflows.string_sub_string_function import StringSubStringFunction
    from simscale_sdk_v1.models.workflows.string_to_integer_value_conversion import StringToIntegerValueConversion
    from simscale_sdk_v1.models.workflows.string_to_real_value_conversion import StringToRealValueConversion
    from simscale_sdk_v1.models.workflows.string_upper_case_function import StringUpperCaseFunction
    from simscale_sdk_v1.models.workflows.string_value import StringValue
    from simscale_sdk_v1.models.workflows.title_ui_type import TitleUiType
    from simscale_sdk_v1.models.workflows.ui_configuration_entry import UiConfigurationEntry
    from simscale_sdk_v1.models.workflows.unit_profile_dimension import UnitProfileDimension
    from simscale_sdk_v1.models.workflows.unit_profiles_dimension import UnitProfilesDimension
    from simscale_sdk_v1.models.workflows.unknown_ui_configuration_entry import UnknownUiConfigurationEntry
    from simscale_sdk_v1.models.workflows.value import Value
    from simscale_sdk_v1.models.workflows.value_list import ValueList
    from simscale_sdk_v1.models.workflows.value_list_data_series_value import ValueListDataSeriesValue
    from simscale_sdk_v1.models.workflows.value_list_enum_value import ValueListEnumValue
    from simscale_sdk_v1.models.workflows.value_list_expression_select import ValueListExpressionSelect
    from simscale_sdk_v1.models.workflows.value_list_function_all import ValueListFunctionAll
    from simscale_sdk_v1.models.workflows.value_list_function_any import ValueListFunctionAny
    from simscale_sdk_v1.models.workflows.value_list_function_drop import ValueListFunctionDrop
    from simscale_sdk_v1.models.workflows.value_list_function_drop_last import ValueListFunctionDropLast
    from simscale_sdk_v1.models.workflows.value_list_function_filter import ValueListFunctionFilter
    from simscale_sdk_v1.models.workflows.value_list_function_find import ValueListFunctionFind
    from simscale_sdk_v1.models.workflows.value_list_function_first import ValueListFunctionFirst
    from simscale_sdk_v1.models.workflows.value_list_function_get import ValueListFunctionGet
    from simscale_sdk_v1.models.workflows.value_list_function_integer_sum import ValueListFunctionIntegerSum
    from simscale_sdk_v1.models.workflows.value_list_function_is_empty import ValueListFunctionIsEmpty
    from simscale_sdk_v1.models.workflows.value_list_function_is_not_empty import ValueListFunctionIsNotEmpty
    from simscale_sdk_v1.models.workflows.value_list_function_last import ValueListFunctionLast
    from simscale_sdk_v1.models.workflows.value_list_function_map import ValueListFunctionMap
    from simscale_sdk_v1.models.workflows.value_list_function_none import ValueListFunctionNone
    from simscale_sdk_v1.models.workflows.value_list_function_real_sum import ValueListFunctionRealSum
    from simscale_sdk_v1.models.workflows.value_list_function_size import ValueListFunctionSize
    from simscale_sdk_v1.models.workflows.value_list_function_sub_list import ValueListFunctionSubList
    from simscale_sdk_v1.models.workflows.value_list_function_take import ValueListFunctionTake
    from simscale_sdk_v1.models.workflows.value_list_function_take_last import ValueListFunctionTakeLast
    from simscale_sdk_v1.models.workflows.value_list_integer_value import ValueListIntegerValue
    from simscale_sdk_v1.models.workflows.value_list_operation_plus import ValueListOperationPlus
    from simscale_sdk_v1.models.workflows.value_list_operation_times import ValueListOperationTimes
    from simscale_sdk_v1.models.workflows.value_list_real_value import ValueListRealValue
    from simscale_sdk_v1.models.workflows.value_list_scaling_point_value_model import ValueListScalingPointValueModel
    from simscale_sdk_v1.models.workflows.value_list_string_value import ValueListStringValue
    from simscale_sdk_v1.models.workflows.value_list_time_by_arch_value_model import ValueListTimeByArchValueModel
    from simscale_sdk_v1.models.workflows.value_list_time_by_gpu_arch_and_model_value_model import (
        ValueListTimeByGpuArchAndModelValueModel,
    )
    from simscale_sdk_v1.models.workflows.value_list_time_by_gpu_arch_value_model import (
        ValueListTimeByGpuArchValueModel,
    )
    from simscale_sdk_v1.models.workflows.value_list_to_string_value_conversion import ValueListToStringValueConversion
    from simscale_sdk_v1.models.workflows.value_list_value import ValueListValue
    from simscale_sdk_v1.models.workflows.value_reference import ValueReference
    from simscale_sdk_v1.models.workflows.vector import Vector
    from simscale_sdk_v1.models.workflows.visibility_ui_configuration_entry import VisibilityUiConfigurationEntry

_NAMES: dict[str, tuple[str, str]] = {
    "AbstractCompoundField": ("simscale_sdk_v1.models.workflows.abstract_compound_field", "AbstractCompoundField"),
    "AbstractCompoundValue": ("simscale_sdk_v1.models.workflows.abstract_compound_value", "AbstractCompoundValue"),
    "AbstractDataDefinition": ("simscale_sdk_v1.models.workflows.abstract_data_definition", "AbstractDataDefinition"),
    "AbstractOperationDefinition": (
        "simscale_sdk_v1.models.workflows.abstract_operation_definition",
        "AbstractOperationDefinition",
    ),
    "AsBooleanValue": ("simscale_sdk_v1.models.workflows.as_boolean_value", "AsBooleanValue"),
    "AsDimensionalScalarValue": (
        "simscale_sdk_v1.models.workflows.as_dimensional_scalar_value",
        "AsDimensionalScalarValue",
    ),
    "AsDimensionalVectorValue": (
        "simscale_sdk_v1.models.workflows.as_dimensional_vector_value",
        "AsDimensionalVectorValue",
    ),
    "AsEntityAssignmentListValue": (
        "simscale_sdk_v1.models.workflows.as_entity_assignment_list_value",
        "AsEntityAssignmentListValue",
    ),
    "AsEntityAssignmentValue": (
        "simscale_sdk_v1.models.workflows.as_entity_assignment_value",
        "AsEntityAssignmentValue",
    ),
    "AsEnumValue": ("simscale_sdk_v1.models.workflows.as_enum_value", "AsEnumValue"),
    "AsIntegerValue": ("simscale_sdk_v1.models.workflows.as_integer_value", "AsIntegerValue"),
    "AsMeasurementUnitValue": ("simscale_sdk_v1.models.workflows.as_measurement_unit_value", "AsMeasurementUnitValue"),
    "AsRealValue": ("simscale_sdk_v1.models.workflows.as_real_value", "AsRealValue"),
    "AsStringValue": ("simscale_sdk_v1.models.workflows.as_string_value", "AsStringValue"),
    "AsValueList": ("simscale_sdk_v1.models.workflows.as_value_list", "AsValueList"),
    "AtomicField": ("simscale_sdk_v1.models.workflows.atomic_field", "AtomicField"),
    "AtomicOperationDefinition": (
        "simscale_sdk_v1.models.workflows.atomic_operation_definition",
        "AtomicOperationDefinition",
    ),
    "BooleanComparisonEqual": ("simscale_sdk_v1.models.workflows.boolean_comparison_equal", "BooleanComparisonEqual"),
    "BooleanComparisonNotEqual": (
        "simscale_sdk_v1.models.workflows.boolean_comparison_not_equal",
        "BooleanComparisonNotEqual",
    ),
    "BooleanConstant": ("simscale_sdk_v1.models.workflows.boolean_constant", "BooleanConstant"),
    "BooleanExpressionSelect": (
        "simscale_sdk_v1.models.workflows.boolean_expression_select",
        "BooleanExpressionSelect",
    ),
    "BooleanField": ("simscale_sdk_v1.models.workflows.boolean_field", "BooleanField"),
    "BooleanOperationAnd": ("simscale_sdk_v1.models.workflows.boolean_operation_and", "BooleanOperationAnd"),
    "BooleanOperationNot": ("simscale_sdk_v1.models.workflows.boolean_operation_not", "BooleanOperationNot"),
    "BooleanOperationOr": ("simscale_sdk_v1.models.workflows.boolean_operation_or", "BooleanOperationOr"),
    "BooleanOperationXor": ("simscale_sdk_v1.models.workflows.boolean_operation_xor", "BooleanOperationXor"),
    "BooleanReference": ("simscale_sdk_v1.models.workflows.boolean_reference", "BooleanReference"),
    "BooleanToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.boolean_to_string_value_conversion",
        "BooleanToStringValueConversion",
    ),
    "BooleanValue": ("simscale_sdk_v1.models.workflows.boolean_value", "BooleanValue"),
    "Breakpoint": ("simscale_sdk_v1.models.workflows.breakpoint", "Breakpoint"),
    "CompoundComparisonEqual": (
        "simscale_sdk_v1.models.workflows.compound_comparison_equal",
        "CompoundComparisonEqual",
    ),
    "CompoundExpressionSelect": (
        "simscale_sdk_v1.models.workflows.compound_expression_select",
        "CompoundExpressionSelect",
    ),
    "CompoundField": ("simscale_sdk_v1.models.workflows.compound_field", "CompoundField"),
    "CompoundFieldCustomUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.compound_field_custom_ui_configuration_entry",
        "CompoundFieldCustomUiConfigurationEntry",
    ),
    "CompoundFieldTitleUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.compound_field_title_ui_configuration_entry",
        "CompoundFieldTitleUiConfigurationEntry",
    ),
    "CompoundMapEntities": ("simscale_sdk_v1.models.workflows.compound_map_entities", "CompoundMapEntities"),
    "CompoundValue": ("simscale_sdk_v1.models.workflows.compound_value", "CompoundValue"),
    "ConfigValueReference": ("simscale_sdk_v1.models.workflows.config_value_reference", "ConfigValueReference"),
    "ConstantValueList": ("simscale_sdk_v1.models.workflows.constant_value_list", "ConstantValueList"),
    "DataMappingEntry": ("simscale_sdk_v1.models.workflows.data_mapping_entry", "DataMappingEntry"),
    "DataPresenceReference": ("simscale_sdk_v1.models.workflows.data_presence_reference", "DataPresenceReference"),
    "DataReference": ("simscale_sdk_v1.models.workflows.data_reference", "DataReference"),
    "DataValueReference": ("simscale_sdk_v1.models.workflows.data_value_reference", "DataValueReference"),
    "DimensionalField": ("simscale_sdk_v1.models.workflows.dimensional_field", "DimensionalField"),
    "DimensionalProfileObjectDimension": (
        "simscale_sdk_v1.models.workflows.dimensional_profile_object_dimension",
        "DimensionalProfileObjectDimension",
    ),
    "DimensionalProfilesObjectDimension": (
        "simscale_sdk_v1.models.workflows.dimensional_profiles_object_dimension",
        "DimensionalProfilesObjectDimension",
    ),
    "DimensionalScalar": ("simscale_sdk_v1.models.workflows.dimensional_scalar", "DimensionalScalar"),
    "DimensionalScalarComparisonGreaterThan": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_greater_than",
        "DimensionalScalarComparisonGreaterThan",
    ),
    "DimensionalScalarComparisonGreaterThanOrEqual": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_greater_than_or_equal",
        "DimensionalScalarComparisonGreaterThanOrEqual",
    ),
    "DimensionalScalarComparisonLessThan": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_less_than",
        "DimensionalScalarComparisonLessThan",
    ),
    "DimensionalScalarComparisonLessThanOrEqual": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_comparison_less_than_or_equal",
        "DimensionalScalarComparisonLessThanOrEqual",
    ),
    "DimensionalScalarConstant": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_constant",
        "DimensionalScalarConstant",
    ),
    "DimensionalScalarExpressionSelect": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_expression_select",
        "DimensionalScalarExpressionSelect",
    ),
    "DimensionalScalarFromDimensionalVectorComponent": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_from_dimensional_vector_component",
        "DimensionalScalarFromDimensionalVectorComponent",
    ),
    "DimensionalScalarFunctionPow": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_function_pow",
        "DimensionalScalarFunctionPow",
    ),
    "DimensionalScalarObject": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_object",
        "DimensionalScalarObject",
    ),
    "DimensionalScalarOperationDiv": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_operation_div",
        "DimensionalScalarOperationDiv",
    ),
    "DimensionalScalarOperationMinus": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_operation_minus",
        "DimensionalScalarOperationMinus",
    ),
    "DimensionalScalarOperationPlus": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_operation_plus",
        "DimensionalScalarOperationPlus",
    ),
    "DimensionalScalarOperationTimes": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_operation_times",
        "DimensionalScalarOperationTimes",
    ),
    "DimensionalScalarReference": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_reference",
        "DimensionalScalarReference",
    ),
    "DimensionalScalarToRealValueConversion": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_to_real_value_conversion",
        "DimensionalScalarToRealValueConversion",
    ),
    "DimensionalScalarToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.dimensional_scalar_to_string_value_conversion",
        "DimensionalScalarToStringValueConversion",
    ),
    "DimensionalScalarValue": ("simscale_sdk_v1.models.workflows.dimensional_scalar_value", "DimensionalScalarValue"),
    "DimensionalVector": ("simscale_sdk_v1.models.workflows.dimensional_vector", "DimensionalVector"),
    "DimensionalVectorConstant": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_constant",
        "DimensionalVectorConstant",
    ),
    "DimensionalVectorExpressionSelect": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_expression_select",
        "DimensionalVectorExpressionSelect",
    ),
    "DimensionalVectorFromComponents": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_from_components",
        "DimensionalVectorFromComponents",
    ),
    "DimensionalVectorFunctionMag": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_function_mag",
        "DimensionalVectorFunctionMag",
    ),
    "DimensionalVectorFunctionNorm": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_function_norm",
        "DimensionalVectorFunctionNorm",
    ),
    "DimensionalVectorObject": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_object",
        "DimensionalVectorObject",
    ),
    "DimensionalVectorOperationDiv": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_operation_div",
        "DimensionalVectorOperationDiv",
    ),
    "DimensionalVectorOperationMinus": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_operation_minus",
        "DimensionalVectorOperationMinus",
    ),
    "DimensionalVectorOperationPlus": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_operation_plus",
        "DimensionalVectorOperationPlus",
    ),
    "DimensionalVectorOperationTimes": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_operation_times",
        "DimensionalVectorOperationTimes",
    ),
    "DimensionalVectorReference": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_reference",
        "DimensionalVectorReference",
    ),
    "DimensionalVectorToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.dimensional_vector_to_string_value_conversion",
        "DimensionalVectorToStringValueConversion",
    ),
    "DimensionalVectorValue": ("simscale_sdk_v1.models.workflows.dimensional_vector_value", "DimensionalVectorValue"),
    "EntityAssignment": ("simscale_sdk_v1.models.workflows.entity_assignment", "EntityAssignment"),
    "EntityAssignmentConstant": (
        "simscale_sdk_v1.models.workflows.entity_assignment_constant",
        "EntityAssignmentConstant",
    ),
    "EntityAssignmentField": ("simscale_sdk_v1.models.workflows.entity_assignment_field", "EntityAssignmentField"),
    "EntityAssignmentFunctionIsEmpty": (
        "simscale_sdk_v1.models.workflows.entity_assignment_function_is_empty",
        "EntityAssignmentFunctionIsEmpty",
    ),
    "EntityAssignmentList": ("simscale_sdk_v1.models.workflows.entity_assignment_list", "EntityAssignmentList"),
    "EntityAssignmentListConstant": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_constant",
        "EntityAssignmentListConstant",
    ),
    "EntityAssignmentListFromComponents": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_from_components",
        "EntityAssignmentListFromComponents",
    ),
    "EntityAssignmentListFunctionCountEntities": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_function_count_entities",
        "EntityAssignmentListFunctionCountEntities",
    ),
    "EntityAssignmentListFunctionIsEmpty": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_function_is_empty",
        "EntityAssignmentListFunctionIsEmpty",
    ),
    "EntityAssignmentListIntersect": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_intersect",
        "EntityAssignmentListIntersect",
    ),
    "EntityAssignmentListMapEntities": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_map_entities",
        "EntityAssignmentListMapEntities",
    ),
    "EntityAssignmentListReference": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_reference",
        "EntityAssignmentListReference",
    ),
    "EntityAssignmentListToMarkdownLinkValueConversion": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_to_markdown_link_value_conversion",
        "EntityAssignmentListToMarkdownLinkValueConversion",
    ),
    "EntityAssignmentListValue": (
        "simscale_sdk_v1.models.workflows.entity_assignment_list_value",
        "EntityAssignmentListValue",
    ),
    "EntityAssignmentMapEntities": (
        "simscale_sdk_v1.models.workflows.entity_assignment_map_entities",
        "EntityAssignmentMapEntities",
    ),
    "EntityAssignmentReference": (
        "simscale_sdk_v1.models.workflows.entity_assignment_reference",
        "EntityAssignmentReference",
    ),
    "EntityAssignmentSource": ("simscale_sdk_v1.models.workflows.entity_assignment_source", "EntityAssignmentSource"),
    "EntityAssignmentToEntityAssignmentListValueConversion": (
        "simscale_sdk_v1.models.workflows.entity_assignment_to_entity_assignment_list_value_conversion",
        "EntityAssignmentToEntityAssignmentListValueConversion",
    ),
    "EntityAssignmentToMarkdownLinkValueConversion": (
        "simscale_sdk_v1.models.workflows.entity_assignment_to_markdown_link_value_conversion",
        "EntityAssignmentToMarkdownLinkValueConversion",
    ),
    "EntityAssignmentToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.entity_assignment_to_string_value_conversion",
        "EntityAssignmentToStringValueConversion",
    ),
    "EntityAssignmentValue": ("simscale_sdk_v1.models.workflows.entity_assignment_value", "EntityAssignmentValue"),
    "EnumComparisonEqual": ("simscale_sdk_v1.models.workflows.enum_comparison_equal", "EnumComparisonEqual"),
    "EnumComparisonNotEqual": ("simscale_sdk_v1.models.workflows.enum_comparison_not_equal", "EnumComparisonNotEqual"),
    "EnumConstant": ("simscale_sdk_v1.models.workflows.enum_constant", "EnumConstant"),
    "EnumExpressionSelect": ("simscale_sdk_v1.models.workflows.enum_expression_select", "EnumExpressionSelect"),
    "EnumField": ("simscale_sdk_v1.models.workflows.enum_field", "EnumField"),
    "EnumFunctionOneOf": ("simscale_sdk_v1.models.workflows.enum_function_one_of", "EnumFunctionOneOf"),
    "EnumReference": ("simscale_sdk_v1.models.workflows.enum_reference", "EnumReference"),
    "EnumToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.enum_to_string_value_conversion",
        "EnumToStringValueConversion",
    ),
    "EnumValue": ("simscale_sdk_v1.models.workflows.enum_value", "EnumValue"),
    "EnumValueDoc": ("simscale_sdk_v1.models.workflows.enum_value_doc", "EnumValueDoc"),
    "EnumValueLabel": ("simscale_sdk_v1.models.workflows.enum_value_label", "EnumValueLabel"),
    "GeneralMetadataValueReference": (
        "simscale_sdk_v1.models.workflows.general_metadata_value_reference",
        "GeneralMetadataValueReference",
    ),
    "GpuScalingEstimationValueModel": (
        "simscale_sdk_v1.models.workflows.gpu_scaling_estimation_value_model",
        "GpuScalingEstimationValueModel",
    ),
    "InlineOperationDefinition": (
        "simscale_sdk_v1.models.workflows.inline_operation_definition",
        "InlineOperationDefinition",
    ),
    "InputDataDefinition": ("simscale_sdk_v1.models.workflows.input_data_definition", "InputDataDefinition"),
    "IntegerComparisonEqual": ("simscale_sdk_v1.models.workflows.integer_comparison_equal", "IntegerComparisonEqual"),
    "IntegerComparisonGreaterThan": (
        "simscale_sdk_v1.models.workflows.integer_comparison_greater_than",
        "IntegerComparisonGreaterThan",
    ),
    "IntegerComparisonGreaterThanOrEqual": (
        "simscale_sdk_v1.models.workflows.integer_comparison_greater_than_or_equal",
        "IntegerComparisonGreaterThanOrEqual",
    ),
    "IntegerComparisonLessThan": (
        "simscale_sdk_v1.models.workflows.integer_comparison_less_than",
        "IntegerComparisonLessThan",
    ),
    "IntegerComparisonLessThanOrEqual": (
        "simscale_sdk_v1.models.workflows.integer_comparison_less_than_or_equal",
        "IntegerComparisonLessThanOrEqual",
    ),
    "IntegerComparisonNotEqual": (
        "simscale_sdk_v1.models.workflows.integer_comparison_not_equal",
        "IntegerComparisonNotEqual",
    ),
    "IntegerConstant": ("simscale_sdk_v1.models.workflows.integer_constant", "IntegerConstant"),
    "IntegerExpressionSelect": (
        "simscale_sdk_v1.models.workflows.integer_expression_select",
        "IntegerExpressionSelect",
    ),
    "IntegerField": ("simscale_sdk_v1.models.workflows.integer_field", "IntegerField"),
    "IntegerFunctionAbs": ("simscale_sdk_v1.models.workflows.integer_function_abs", "IntegerFunctionAbs"),
    "IntegerFunctionMax": ("simscale_sdk_v1.models.workflows.integer_function_max", "IntegerFunctionMax"),
    "IntegerFunctionMin": ("simscale_sdk_v1.models.workflows.integer_function_min", "IntegerFunctionMin"),
    "IntegerOperationDiv": ("simscale_sdk_v1.models.workflows.integer_operation_div", "IntegerOperationDiv"),
    "IntegerOperationMinus": ("simscale_sdk_v1.models.workflows.integer_operation_minus", "IntegerOperationMinus"),
    "IntegerOperationPlus": ("simscale_sdk_v1.models.workflows.integer_operation_plus", "IntegerOperationPlus"),
    "IntegerOperationRem": ("simscale_sdk_v1.models.workflows.integer_operation_rem", "IntegerOperationRem"),
    "IntegerOperationTimes": ("simscale_sdk_v1.models.workflows.integer_operation_times", "IntegerOperationTimes"),
    "IntegerReference": ("simscale_sdk_v1.models.workflows.integer_reference", "IntegerReference"),
    "IntegerSequenceGenerator": (
        "simscale_sdk_v1.models.workflows.integer_sequence_generator",
        "IntegerSequenceGenerator",
    ),
    "IntegerToDimensionalScalarValueConversion": (
        "simscale_sdk_v1.models.workflows.integer_to_dimensional_scalar_value_conversion",
        "IntegerToDimensionalScalarValueConversion",
    ),
    "IntegerToRealValueConversion": (
        "simscale_sdk_v1.models.workflows.integer_to_real_value_conversion",
        "IntegerToRealValueConversion",
    ),
    "IntegerToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.integer_to_string_value_conversion",
        "IntegerToStringValueConversion",
    ),
    "IntegerValue": ("simscale_sdk_v1.models.workflows.integer_value", "IntegerValue"),
    "IntermediateDataDefinition": (
        "simscale_sdk_v1.models.workflows.intermediate_data_definition",
        "IntermediateDataDefinition",
    ),
    "IteratorReference": ("simscale_sdk_v1.models.workflows.iterator_reference", "IteratorReference"),
    "JsonNode": ("simscale_sdk_v1.models.workflows.json_node", "JsonNode"),
    "MeasurementUnitComparisonEqual": (
        "simscale_sdk_v1.models.workflows.measurement_unit_comparison_equal",
        "MeasurementUnitComparisonEqual",
    ),
    "MeasurementUnitComparisonNotEqual": (
        "simscale_sdk_v1.models.workflows.measurement_unit_comparison_not_equal",
        "MeasurementUnitComparisonNotEqual",
    ),
    "MeasurementUnitConstant": (
        "simscale_sdk_v1.models.workflows.measurement_unit_constant",
        "MeasurementUnitConstant",
    ),
    "MeasurementUnitExpressionSelect": (
        "simscale_sdk_v1.models.workflows.measurement_unit_expression_select",
        "MeasurementUnitExpressionSelect",
    ),
    "MeasurementUnitField": ("simscale_sdk_v1.models.workflows.measurement_unit_field", "MeasurementUnitField"),
    "MeasurementUnitFunctionPow": (
        "simscale_sdk_v1.models.workflows.measurement_unit_function_pow",
        "MeasurementUnitFunctionPow",
    ),
    "MeasurementUnitOperationDiv": (
        "simscale_sdk_v1.models.workflows.measurement_unit_operation_div",
        "MeasurementUnitOperationDiv",
    ),
    "MeasurementUnitOperationTimes": (
        "simscale_sdk_v1.models.workflows.measurement_unit_operation_times",
        "MeasurementUnitOperationTimes",
    ),
    "MeasurementUnitReference": (
        "simscale_sdk_v1.models.workflows.measurement_unit_reference",
        "MeasurementUnitReference",
    ),
    "MeasurementUnitValue": ("simscale_sdk_v1.models.workflows.measurement_unit_value", "MeasurementUnitValue"),
    "MetadataValueReference": ("simscale_sdk_v1.models.workflows.metadata_value_reference", "MetadataValueReference"),
    "MethodOperationDefinition": (
        "simscale_sdk_v1.models.workflows.method_operation_definition",
        "MethodOperationDefinition",
    ),
    "MethodResourceEstimationValueModel": (
        "simscale_sdk_v1.models.workflows.method_resource_estimation_value_model",
        "MethodResourceEstimationValueModel",
    ),
    "NavigationListUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.navigation_list_ui_configuration_entry",
        "NavigationListUiConfigurationEntry",
    ),
    "NavigationUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.navigation_ui_configuration_entry",
        "NavigationUiConfigurationEntry",
    ),
    "NestedSchemaField": ("simscale_sdk_v1.models.workflows.nested_schema_field", "NestedSchemaField"),
    "NestedWorkflowOperationDefinition": (
        "simscale_sdk_v1.models.workflows.nested_workflow_operation_definition",
        "NestedWorkflowOperationDefinition",
    ),
    "OneGpuEstimationValueModel": (
        "simscale_sdk_v1.models.workflows.one_gpu_estimation_value_model",
        "OneGpuEstimationValueModel",
    ),
    "OneProcessorEstimationValueModel": (
        "simscale_sdk_v1.models.workflows.one_processor_estimation_value_model",
        "OneProcessorEstimationValueModel",
    ),
    "OperationGroupDefinition": (
        "simscale_sdk_v1.models.workflows.operation_group_definition",
        "OperationGroupDefinition",
    ),
    "OperationGroupWithConditionDefinition": (
        "simscale_sdk_v1.models.workflows.operation_group_with_condition_definition",
        "OperationGroupWithConditionDefinition",
    ),
    "OperationGroupWithParameterDefinition": (
        "simscale_sdk_v1.models.workflows.operation_group_with_parameter_definition",
        "OperationGroupWithParameterDefinition",
    ),
    "OutputDataDefinition": ("simscale_sdk_v1.models.workflows.output_data_definition", "OutputDataDefinition"),
    "PairBooleanValueAbstractCompoundValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_abstract_compound_value",
        "PairBooleanValueAbstractCompoundValue",
    ),
    "PairBooleanValueBooleanValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_boolean_value",
        "PairBooleanValueBooleanValue",
    ),
    "PairBooleanValueDimensionalScalarValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_dimensional_scalar_value",
        "PairBooleanValueDimensionalScalarValue",
    ),
    "PairBooleanValueDimensionalVectorValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_dimensional_vector_value",
        "PairBooleanValueDimensionalVectorValue",
    ),
    "PairBooleanValueEnumValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_enum_value",
        "PairBooleanValueEnumValue",
    ),
    "PairBooleanValueIntegerValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_integer_value",
        "PairBooleanValueIntegerValue",
    ),
    "PairBooleanValueMeasurementUnitValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_measurement_unit_value",
        "PairBooleanValueMeasurementUnitValue",
    ),
    "PairBooleanValueRealValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_real_value",
        "PairBooleanValueRealValue",
    ),
    "PairBooleanValueStringValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_string_value",
        "PairBooleanValueStringValue",
    ),
    "PairBooleanValueValueListValue": (
        "simscale_sdk_v1.models.workflows.pair_boolean_value_value_list_value",
        "PairBooleanValueValueListValue",
    ),
    "ParameterValueCombination": (
        "simscale_sdk_v1.models.workflows.parameter_value_combination",
        "ParameterValueCombination",
    ),
    "Plot2DUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.plot2_d_ui_configuration_entry",
        "Plot2DUiConfigurationEntry",
    ),
    "PolymorphicCompoundTypeCheck": (
        "simscale_sdk_v1.models.workflows.polymorphic_compound_type_check",
        "PolymorphicCompoundTypeCheck",
    ),
    "RealComparisonEqual": ("simscale_sdk_v1.models.workflows.real_comparison_equal", "RealComparisonEqual"),
    "RealComparisonGreaterThan": (
        "simscale_sdk_v1.models.workflows.real_comparison_greater_than",
        "RealComparisonGreaterThan",
    ),
    "RealComparisonGreaterThanOrEqual": (
        "simscale_sdk_v1.models.workflows.real_comparison_greater_than_or_equal",
        "RealComparisonGreaterThanOrEqual",
    ),
    "RealComparisonLessThan": ("simscale_sdk_v1.models.workflows.real_comparison_less_than", "RealComparisonLessThan"),
    "RealComparisonLessThanOrEqual": (
        "simscale_sdk_v1.models.workflows.real_comparison_less_than_or_equal",
        "RealComparisonLessThanOrEqual",
    ),
    "RealComparisonNotEqual": ("simscale_sdk_v1.models.workflows.real_comparison_not_equal", "RealComparisonNotEqual"),
    "RealConstant": ("simscale_sdk_v1.models.workflows.real_constant", "RealConstant"),
    "RealExpressionSelect": ("simscale_sdk_v1.models.workflows.real_expression_select", "RealExpressionSelect"),
    "RealField": ("simscale_sdk_v1.models.workflows.real_field", "RealField"),
    "RealFunctionACos": ("simscale_sdk_v1.models.workflows.real_function_a_cos", "RealFunctionACos"),
    "RealFunctionASin": ("simscale_sdk_v1.models.workflows.real_function_a_sin", "RealFunctionASin"),
    "RealFunctionATan": ("simscale_sdk_v1.models.workflows.real_function_a_tan", "RealFunctionATan"),
    "RealFunctionATan2": ("simscale_sdk_v1.models.workflows.real_function_a_tan2", "RealFunctionATan2"),
    "RealFunctionAbs": ("simscale_sdk_v1.models.workflows.real_function_abs", "RealFunctionAbs"),
    "RealFunctionCbrt": ("simscale_sdk_v1.models.workflows.real_function_cbrt", "RealFunctionCbrt"),
    "RealFunctionCos": ("simscale_sdk_v1.models.workflows.real_function_cos", "RealFunctionCos"),
    "RealFunctionExp": ("simscale_sdk_v1.models.workflows.real_function_exp", "RealFunctionExp"),
    "RealFunctionLog": ("simscale_sdk_v1.models.workflows.real_function_log", "RealFunctionLog"),
    "RealFunctionLog10": ("simscale_sdk_v1.models.workflows.real_function_log10", "RealFunctionLog10"),
    "RealFunctionMax": ("simscale_sdk_v1.models.workflows.real_function_max", "RealFunctionMax"),
    "RealFunctionMin": ("simscale_sdk_v1.models.workflows.real_function_min", "RealFunctionMin"),
    "RealFunctionPow": ("simscale_sdk_v1.models.workflows.real_function_pow", "RealFunctionPow"),
    "RealFunctionSin": ("simscale_sdk_v1.models.workflows.real_function_sin", "RealFunctionSin"),
    "RealFunctionSqrt": ("simscale_sdk_v1.models.workflows.real_function_sqrt", "RealFunctionSqrt"),
    "RealFunctionTan": ("simscale_sdk_v1.models.workflows.real_function_tan", "RealFunctionTan"),
    "RealOperationDiv": ("simscale_sdk_v1.models.workflows.real_operation_div", "RealOperationDiv"),
    "RealOperationMinus": ("simscale_sdk_v1.models.workflows.real_operation_minus", "RealOperationMinus"),
    "RealOperationPlus": ("simscale_sdk_v1.models.workflows.real_operation_plus", "RealOperationPlus"),
    "RealOperationTimes": ("simscale_sdk_v1.models.workflows.real_operation_times", "RealOperationTimes"),
    "RealReference": ("simscale_sdk_v1.models.workflows.real_reference", "RealReference"),
    "RealSequenceGenerator": ("simscale_sdk_v1.models.workflows.real_sequence_generator", "RealSequenceGenerator"),
    "RealToDimensionalScalarValueConversion": (
        "simscale_sdk_v1.models.workflows.real_to_dimensional_scalar_value_conversion",
        "RealToDimensionalScalarValueConversion",
    ),
    "RealToIntegerConversion": (
        "simscale_sdk_v1.models.workflows.real_to_integer_conversion",
        "RealToIntegerConversion",
    ),
    "RealToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.real_to_string_value_conversion",
        "RealToStringValueConversion",
    ),
    "RealValue": ("simscale_sdk_v1.models.workflows.real_value", "RealValue"),
    "ReferenceValueList": ("simscale_sdk_v1.models.workflows.reference_value_list", "ReferenceValueList"),
    "ScalingEstimationValueModel": (
        "simscale_sdk_v1.models.workflows.scaling_estimation_value_model",
        "ScalingEstimationValueModel",
    ),
    "SchemaDefinition": ("simscale_sdk_v1.models.workflows.schema_definition", "SchemaDefinition"),
    "SchemaElement": ("simscale_sdk_v1.models.workflows.schema_element", "SchemaElement"),
    "SerializableDataMap": ("simscale_sdk_v1.models.workflows.serializable_data_map", "SerializableDataMap"),
    "SliderUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.slider_ui_configuration_entry",
        "SliderUiConfigurationEntry",
    ),
    "StringComparisonEqual": ("simscale_sdk_v1.models.workflows.string_comparison_equal", "StringComparisonEqual"),
    "StringComparisonNotEqual": (
        "simscale_sdk_v1.models.workflows.string_comparison_not_equal",
        "StringComparisonNotEqual",
    ),
    "StringConstant": ("simscale_sdk_v1.models.workflows.string_constant", "StringConstant"),
    "StringContainsFunction": ("simscale_sdk_v1.models.workflows.string_contains_function", "StringContainsFunction"),
    "StringEndsWithFunction": ("simscale_sdk_v1.models.workflows.string_ends_with_function", "StringEndsWithFunction"),
    "StringExpressionSelect": ("simscale_sdk_v1.models.workflows.string_expression_select", "StringExpressionSelect"),
    "StringField": ("simscale_sdk_v1.models.workflows.string_field", "StringField"),
    "StringLengthFunction": ("simscale_sdk_v1.models.workflows.string_length_function", "StringLengthFunction"),
    "StringLowerCaseFunction": (
        "simscale_sdk_v1.models.workflows.string_lower_case_function",
        "StringLowerCaseFunction",
    ),
    "StringOperationPlus": ("simscale_sdk_v1.models.workflows.string_operation_plus", "StringOperationPlus"),
    "StringReference": ("simscale_sdk_v1.models.workflows.string_reference", "StringReference"),
    "StringStartsWithFunction": (
        "simscale_sdk_v1.models.workflows.string_starts_with_function",
        "StringStartsWithFunction",
    ),
    "StringSubStringFunction": (
        "simscale_sdk_v1.models.workflows.string_sub_string_function",
        "StringSubStringFunction",
    ),
    "StringToIntegerValueConversion": (
        "simscale_sdk_v1.models.workflows.string_to_integer_value_conversion",
        "StringToIntegerValueConversion",
    ),
    "StringToRealValueConversion": (
        "simscale_sdk_v1.models.workflows.string_to_real_value_conversion",
        "StringToRealValueConversion",
    ),
    "StringUpperCaseFunction": (
        "simscale_sdk_v1.models.workflows.string_upper_case_function",
        "StringUpperCaseFunction",
    ),
    "StringValue": ("simscale_sdk_v1.models.workflows.string_value", "StringValue"),
    "TitleUiType": ("simscale_sdk_v1.models.workflows.title_ui_type", "TitleUiType"),
    "UiConfigurationEntry": ("simscale_sdk_v1.models.workflows.ui_configuration_entry", "UiConfigurationEntry"),
    "UnitProfileDimension": ("simscale_sdk_v1.models.workflows.unit_profile_dimension", "UnitProfileDimension"),
    "UnitProfilesDimension": ("simscale_sdk_v1.models.workflows.unit_profiles_dimension", "UnitProfilesDimension"),
    "UnknownUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.unknown_ui_configuration_entry",
        "UnknownUiConfigurationEntry",
    ),
    "Value": ("simscale_sdk_v1.models.workflows.value", "Value"),
    "ValueList": ("simscale_sdk_v1.models.workflows.value_list", "ValueList"),
    "ValueListDataSeriesValue": (
        "simscale_sdk_v1.models.workflows.value_list_data_series_value",
        "ValueListDataSeriesValue",
    ),
    "ValueListEnumValue": ("simscale_sdk_v1.models.workflows.value_list_enum_value", "ValueListEnumValue"),
    "ValueListExpressionSelect": (
        "simscale_sdk_v1.models.workflows.value_list_expression_select",
        "ValueListExpressionSelect",
    ),
    "ValueListFunctionAll": ("simscale_sdk_v1.models.workflows.value_list_function_all", "ValueListFunctionAll"),
    "ValueListFunctionAny": ("simscale_sdk_v1.models.workflows.value_list_function_any", "ValueListFunctionAny"),
    "ValueListFunctionDrop": ("simscale_sdk_v1.models.workflows.value_list_function_drop", "ValueListFunctionDrop"),
    "ValueListFunctionDropLast": (
        "simscale_sdk_v1.models.workflows.value_list_function_drop_last",
        "ValueListFunctionDropLast",
    ),
    "ValueListFunctionFilter": (
        "simscale_sdk_v1.models.workflows.value_list_function_filter",
        "ValueListFunctionFilter",
    ),
    "ValueListFunctionFind": ("simscale_sdk_v1.models.workflows.value_list_function_find", "ValueListFunctionFind"),
    "ValueListFunctionFirst": ("simscale_sdk_v1.models.workflows.value_list_function_first", "ValueListFunctionFirst"),
    "ValueListFunctionGet": ("simscale_sdk_v1.models.workflows.value_list_function_get", "ValueListFunctionGet"),
    "ValueListFunctionIntegerSum": (
        "simscale_sdk_v1.models.workflows.value_list_function_integer_sum",
        "ValueListFunctionIntegerSum",
    ),
    "ValueListFunctionIsEmpty": (
        "simscale_sdk_v1.models.workflows.value_list_function_is_empty",
        "ValueListFunctionIsEmpty",
    ),
    "ValueListFunctionIsNotEmpty": (
        "simscale_sdk_v1.models.workflows.value_list_function_is_not_empty",
        "ValueListFunctionIsNotEmpty",
    ),
    "ValueListFunctionLast": ("simscale_sdk_v1.models.workflows.value_list_function_last", "ValueListFunctionLast"),
    "ValueListFunctionMap": ("simscale_sdk_v1.models.workflows.value_list_function_map", "ValueListFunctionMap"),
    "ValueListFunctionNone": ("simscale_sdk_v1.models.workflows.value_list_function_none", "ValueListFunctionNone"),
    "ValueListFunctionRealSum": (
        "simscale_sdk_v1.models.workflows.value_list_function_real_sum",
        "ValueListFunctionRealSum",
    ),
    "ValueListFunctionSize": ("simscale_sdk_v1.models.workflows.value_list_function_size", "ValueListFunctionSize"),
    "ValueListFunctionSubList": (
        "simscale_sdk_v1.models.workflows.value_list_function_sub_list",
        "ValueListFunctionSubList",
    ),
    "ValueListFunctionTake": ("simscale_sdk_v1.models.workflows.value_list_function_take", "ValueListFunctionTake"),
    "ValueListFunctionTakeLast": (
        "simscale_sdk_v1.models.workflows.value_list_function_take_last",
        "ValueListFunctionTakeLast",
    ),
    "ValueListIntegerValue": ("simscale_sdk_v1.models.workflows.value_list_integer_value", "ValueListIntegerValue"),
    "ValueListOperationPlus": ("simscale_sdk_v1.models.workflows.value_list_operation_plus", "ValueListOperationPlus"),
    "ValueListOperationTimes": (
        "simscale_sdk_v1.models.workflows.value_list_operation_times",
        "ValueListOperationTimes",
    ),
    "ValueListRealValue": ("simscale_sdk_v1.models.workflows.value_list_real_value", "ValueListRealValue"),
    "ValueListScalingPointValueModel": (
        "simscale_sdk_v1.models.workflows.value_list_scaling_point_value_model",
        "ValueListScalingPointValueModel",
    ),
    "ValueListStringValue": ("simscale_sdk_v1.models.workflows.value_list_string_value", "ValueListStringValue"),
    "ValueListTimeByArchValueModel": (
        "simscale_sdk_v1.models.workflows.value_list_time_by_arch_value_model",
        "ValueListTimeByArchValueModel",
    ),
    "ValueListTimeByGpuArchAndModelValueModel": (
        "simscale_sdk_v1.models.workflows.value_list_time_by_gpu_arch_and_model_value_model",
        "ValueListTimeByGpuArchAndModelValueModel",
    ),
    "ValueListTimeByGpuArchValueModel": (
        "simscale_sdk_v1.models.workflows.value_list_time_by_gpu_arch_value_model",
        "ValueListTimeByGpuArchValueModel",
    ),
    "ValueListToStringValueConversion": (
        "simscale_sdk_v1.models.workflows.value_list_to_string_value_conversion",
        "ValueListToStringValueConversion",
    ),
    "ValueListValue": ("simscale_sdk_v1.models.workflows.value_list_value", "ValueListValue"),
    "ValueReference": ("simscale_sdk_v1.models.workflows.value_reference", "ValueReference"),
    "Vector": ("simscale_sdk_v1.models.workflows.vector", "Vector"),
    "VisibilityUiConfigurationEntry": (
        "simscale_sdk_v1.models.workflows.visibility_ui_configuration_entry",
        "VisibilityUiConfigurationEntry",
    ),
}


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys())
