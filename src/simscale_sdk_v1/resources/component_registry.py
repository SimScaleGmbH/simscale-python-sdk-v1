from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class ComponentRegistry:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_component_group_metadata(
        self,
        component_group_reference: str,
        *,
        language: str | None = None,
    ) -> models.component_registry.ComponentGroupMetadata:
        """Read the metadata of a component group."""
        return self._client.request(
            "GET",
            f"/component-registry/component-groups/{component_group_reference}",
            query_params={"language": language},
            response_type=models.component_registry.ComponentGroupMetadata,
        )

    def get_component_metadata(
        self,
        component_reference: str,
        *,
        language: str | None = None,
    ) -> models.component_registry.ComponentOverview:
        """Read an overview of a component."""
        return self._client.request(
            "GET",
            f"/component-registry/components/{component_reference}",
            query_params={"language": language},
            response_type=models.component_registry.ComponentOverview,
        )

    def get_component_version_dependencies(
        self,
        component_version_reference: str,
    ) -> models.component_registry.ComponentVersionDependencies:
        """List the dependencies of a component version."""
        return self._client.request(
            "GET",
            f"/component-registry/component-versions/{component_version_reference}/dependencies",
            response_type=models.component_registry.ComponentVersionDependencies,
        )

    def get_component_version_dependents(
        self,
        component_version_reference: str,
    ) -> models.component_registry.ComponentVersionDependents:
        """List the dependents of a component version."""
        return self._client.request(
            "GET",
            f"/component-registry/component-versions/{component_version_reference}/dependents",
            response_type=models.component_registry.ComponentVersionDependents,
        )

    def get_component_version_metadata(
        self,
        component_version_reference: str,
    ) -> models.component_registry.ComponentVersionMetadata:
        """Read the metadata of a component version."""
        return self._client.request(
            "GET",
            f"/component-registry/component-versions/{component_version_reference}",
            response_type=models.component_registry.ComponentVersionMetadata,
        )

    def get_data_type_file_operations(
        self,
        component_version_reference: str,
    ) -> models.component_registry.DataTypeFileOperationsDescription:
        """Read the file-operations description of a data type version."""
        return self._client.request(
            "GET",
            f"/component-registry/data-types/{component_version_reference}/file-operations",
            response_type=models.component_registry.DataTypeFileOperationsDescription,
        )

    def get_data_type_metadata_schema(
        self,
        component_version_reference: str,
        *,
        resolve_dependencies: bool | None = None,
    ) -> models.workflows.SchemaDefinition:
        """Read the metadata schema of a data type version."""
        return self._client.request(
            "GET",
            f"/component-registry/data-types/{component_version_reference}/metadata-schema",
            query_params={"resolveDependencies": resolve_dependencies},
            response_type=models.workflows.SchemaDefinition,
        )

    def get_data_type_metadata_schema_validation_rules(
        self,
        component_version_reference: str,
    ) -> models.component_registry.ValidationRuleSet:
        """Read the metadata schema validation rules of a data type version."""
        return self._client.request(
            "GET",
            f"/component-registry/data-types/{component_version_reference}/metadata-schema-validation-rules",
            response_type=models.component_registry.ValidationRuleSet,
        )

    def get_data_type_schema(
        self,
        component_version_reference: str,
        *,
        resolve_dependencies: bool | None = None,
    ) -> models.workflows.SchemaDefinition:
        """Read the data schema of a data type version."""
        return self._client.request(
            "GET",
            f"/component-registry/data-types/{component_version_reference}/schema",
            query_params={"resolveDependencies": resolve_dependencies},
            response_type=models.workflows.SchemaDefinition,
        )

    def get_data_type_schema_validation_rules(
        self,
        component_version_reference: str,
    ) -> models.component_registry.ValidationRuleSet:
        """Read the data schema validation rules of a data type version."""
        return self._client.request(
            "GET",
            f"/component-registry/data-types/{component_version_reference}/schema-validation-rules",
            response_type=models.component_registry.ValidationRuleSet,
        )

    def get_data_type_ui_schema(
        self,
        component_version_reference: str,
    ) -> models.workflows.SchemaDefinition:
        """Read the UI schema of a data type version."""
        return self._client.request(
            "GET",
            f"/component-registry/data-types/{component_version_reference}/ui-schema",
            response_type=models.workflows.SchemaDefinition,
        )

    def get_method_configuration_schema(
        self,
        component_version_reference: str,
        *,
        resolve_dependencies: bool | None = None,
    ) -> models.workflows.SchemaDefinition:
        """Read the configuration schema of a method version."""
        return self._client.request(
            "GET",
            f"/component-registry/methods/{component_version_reference}/configuration-schema",
            query_params={"resolveDependencies": resolve_dependencies},
            response_type=models.workflows.SchemaDefinition,
        )

    def get_method_configuration_schema_validation_rules(
        self,
        component_version_reference: str,
    ) -> models.component_registry.ValidationRuleSet:
        """Read the configuration schema validation rules of a method version."""
        return self._client.request(
            "GET",
            f"/component-registry/methods/{component_version_reference}/configuration-schema-validation-rules",
            response_type=models.component_registry.ValidationRuleSet,
        )

    def get_method_data_interface(
        self,
        component_version_reference: str,
    ) -> models.component_registry.DataInterface:
        """Read the data interface of a method version."""
        return self._client.request(
            "GET",
            f"/component-registry/methods/{component_version_reference}/data-interface",
            response_type=models.component_registry.DataInterface,
        )

    def get_method_resource_estimation(
        self,
        component_version_reference: str,
    ) -> models.workflows.MethodResourceEstimationValueModel:
        """Read the resource estimation model of a method version."""
        return self._client.request(
            "GET",
            f"/component-registry/methods/{component_version_reference}/resource-estimation",
            response_type=models.workflows.MethodResourceEstimationValueModel,
        )

    def get_organization_component_group_metadata(
        self,
        organization_reference: str,
    ) -> models.component_registry.OrganizationComponentGroupMetadata:
        """Read the metadata of the organization component group."""
        return self._client.request(
            "GET",
            f"/component-registry/organization-component-groups/{organization_reference}",
            response_type=models.component_registry.OrganizationComponentGroupMetadata,
        )

    def get_workflow_type_configuration_schema(
        self,
        component_version_reference: str,
        *,
        resolve_dependencies: bool | None = None,
    ) -> models.workflows.SchemaDefinition:
        """Read the configuration schema of a workflow type version."""
        return self._client.request(
            "GET",
            f"/component-registry/workflow-types/{component_version_reference}/configuration-schema",
            query_params={"resolveDependencies": resolve_dependencies},
            response_type=models.workflows.SchemaDefinition,
        )

    def get_workflow_type_configuration_schema_validation_rules(
        self,
        component_version_reference: str,
    ) -> models.component_registry.ValidationRuleSet:
        """Read the configuration schema validation rules of a workflow type version."""
        return self._client.request(
            "GET",
            f"/component-registry/workflow-types/{component_version_reference}/configuration-schema-validation-rules",
            response_type=models.component_registry.ValidationRuleSet,
        )

    def get_workflow_type_data_interface(
        self,
        component_version_reference: str,
    ) -> models.component_registry.DataInterface:
        """Read the data interface of a workflow type version."""
        return self._client.request(
            "GET",
            f"/component-registry/workflow-types/{component_version_reference}/data-interface",
            response_type=models.component_registry.DataInterface,
        )

    def get_workflow_type_ui_configuration(
        self,
        component_version_reference: str,
    ) -> models.component_registry.UiConfiguration:
        """Read the UI configuration of a workflow type version."""
        return self._client.request(
            "GET",
            f"/component-registry/workflow-types/{component_version_reference}/ui-configuration",
            response_type=models.component_registry.UiConfiguration,
        )

    def get_workflow_type_workflow_definition(
        self,
        component_version_reference: str,
    ) -> models.component_registry.WorkflowDefinition:
        """Read the workflow definition of a workflow type version."""
        return self._client.request(
            "GET",
            f"/component-registry/workflow-types/{component_version_reference}/workflow-definition",
            response_type=models.component_registry.WorkflowDefinition,
        )

    def list_component_subgroups(
        self,
        component_group_reference: str,
        *,
        page: int | None = None,
        size: int | None = None,
    ) -> list[models.component_registry.ComponentGroupMetadata]:
        """List the subgroups of a component group."""
        return self._client.request(
            "GET",
            f"/component-registry/component-groups/{component_group_reference}/subgroups",
            query_params={"page": page, "size": size},
            response_type=list[models.component_registry.ComponentGroupMetadata],
        )

    def list_component_versions(
        self,
        component_reference: str,
        *,
        page: int | None = None,
        size: int | None = None,
    ) -> list[models.component_registry.ComponentVersionMetadata]:
        """List the versions of a component."""
        return self._client.request(
            "GET",
            f"/component-registry/components/{component_reference}/versions",
            query_params={"page": page, "size": size},
            response_type=list[models.component_registry.ComponentVersionMetadata],
        )

    def list_components(
        self,
        component_group_reference: str,
        *,
        page: int | None = None,
        size: int | None = None,
        language: str | None = None,
    ) -> list[models.component_registry.ComponentOverview]:
        """List the components in a component group."""
        return self._client.request(
            "GET",
            f"/component-registry/component-groups/{component_group_reference}/components",
            query_params={"page": page, "size": size, "language": language},
            response_type=list[models.component_registry.ComponentOverview],
        )
