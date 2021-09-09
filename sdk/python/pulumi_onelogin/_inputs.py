# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'AppParameterArgs',
    'AppRuleActionArgs',
    'AppRuleConditionArgs',
    'OidcAppParameterArgs',
    'PrivilegesPrivilegeArgs',
    'PrivilegesPrivilegeStatementArgs',
    'SamlAppParameterArgs',
    'SmartHookConditionArgs',
    'SmartHookOptionsArgs',
    'UserMappingActionArgs',
    'UserMappingConditionArgs',
]

@pulumi.input_type
class AppParameterArgs:
    def __init__(__self__, *,
                 param_key_name: pulumi.Input[str],
                 attributes_transformations: Optional[pulumi.Input[str]] = None,
                 default_values: Optional[pulumi.Input[str]] = None,
                 include_in_saml_assertion: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 param_id: Optional[pulumi.Input[int]] = None,
                 provisioned_entitlements: Optional[pulumi.Input[bool]] = None,
                 safe_entitlements_enabled: Optional[pulumi.Input[bool]] = None,
                 skip_if_blank: Optional[pulumi.Input[bool]] = None,
                 user_attribute_macros: Optional[pulumi.Input[str]] = None,
                 user_attribute_mappings: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "param_key_name", param_key_name)
        if attributes_transformations is not None:
            pulumi.set(__self__, "attributes_transformations", attributes_transformations)
        if default_values is not None:
            pulumi.set(__self__, "default_values", default_values)
        if include_in_saml_assertion is not None:
            pulumi.set(__self__, "include_in_saml_assertion", include_in_saml_assertion)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if param_id is not None:
            pulumi.set(__self__, "param_id", param_id)
        if provisioned_entitlements is not None:
            pulumi.set(__self__, "provisioned_entitlements", provisioned_entitlements)
        if safe_entitlements_enabled is not None:
            pulumi.set(__self__, "safe_entitlements_enabled", safe_entitlements_enabled)
        if skip_if_blank is not None:
            pulumi.set(__self__, "skip_if_blank", skip_if_blank)
        if user_attribute_macros is not None:
            pulumi.set(__self__, "user_attribute_macros", user_attribute_macros)
        if user_attribute_mappings is not None:
            pulumi.set(__self__, "user_attribute_mappings", user_attribute_mappings)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="paramKeyName")
    def param_key_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "param_key_name")

    @param_key_name.setter
    def param_key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "param_key_name", value)

    @property
    @pulumi.getter(name="attributesTransformations")
    def attributes_transformations(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "attributes_transformations")

    @attributes_transformations.setter
    def attributes_transformations(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attributes_transformations", value)

    @property
    @pulumi.getter(name="defaultValues")
    def default_values(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_values")

    @default_values.setter
    def default_values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_values", value)

    @property
    @pulumi.getter(name="includeInSamlAssertion")
    def include_in_saml_assertion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "include_in_saml_assertion")

    @include_in_saml_assertion.setter
    def include_in_saml_assertion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_in_saml_assertion", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="paramId")
    def param_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "param_id")

    @param_id.setter
    def param_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "param_id", value)

    @property
    @pulumi.getter(name="provisionedEntitlements")
    def provisioned_entitlements(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "provisioned_entitlements")

    @provisioned_entitlements.setter
    def provisioned_entitlements(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "provisioned_entitlements", value)

    @property
    @pulumi.getter(name="safeEntitlementsEnabled")
    def safe_entitlements_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "safe_entitlements_enabled")

    @safe_entitlements_enabled.setter
    def safe_entitlements_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "safe_entitlements_enabled", value)

    @property
    @pulumi.getter(name="skipIfBlank")
    def skip_if_blank(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_if_blank")

    @skip_if_blank.setter
    def skip_if_blank(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_if_blank", value)

    @property
    @pulumi.getter(name="userAttributeMacros")
    def user_attribute_macros(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_attribute_macros")

    @user_attribute_macros.setter
    def user_attribute_macros(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute_macros", value)

    @property
    @pulumi.getter(name="userAttributeMappings")
    def user_attribute_mappings(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_attribute_mappings")

    @user_attribute_mappings.setter
    def user_attribute_mappings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute_mappings", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class AppRuleActionArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]],
                 expression: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "values", values)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)


@pulumi.input_type
class AppRuleConditionArgs:
    def __init__(__self__, *,
                 operator: pulumi.Input[str],
                 source: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[str]:
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[str]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class OidcAppParameterArgs:
    def __init__(__self__, *,
                 param_key_name: pulumi.Input[str],
                 attributes_transformations: Optional[pulumi.Input[str]] = None,
                 default_values: Optional[pulumi.Input[str]] = None,
                 include_in_saml_assertion: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 param_id: Optional[pulumi.Input[int]] = None,
                 provisioned_entitlements: Optional[pulumi.Input[bool]] = None,
                 safe_entitlements_enabled: Optional[pulumi.Input[bool]] = None,
                 skip_if_blank: Optional[pulumi.Input[bool]] = None,
                 user_attribute_macros: Optional[pulumi.Input[str]] = None,
                 user_attribute_mappings: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "param_key_name", param_key_name)
        if attributes_transformations is not None:
            pulumi.set(__self__, "attributes_transformations", attributes_transformations)
        if default_values is not None:
            pulumi.set(__self__, "default_values", default_values)
        if include_in_saml_assertion is not None:
            pulumi.set(__self__, "include_in_saml_assertion", include_in_saml_assertion)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if param_id is not None:
            pulumi.set(__self__, "param_id", param_id)
        if provisioned_entitlements is not None:
            pulumi.set(__self__, "provisioned_entitlements", provisioned_entitlements)
        if safe_entitlements_enabled is not None:
            pulumi.set(__self__, "safe_entitlements_enabled", safe_entitlements_enabled)
        if skip_if_blank is not None:
            pulumi.set(__self__, "skip_if_blank", skip_if_blank)
        if user_attribute_macros is not None:
            pulumi.set(__self__, "user_attribute_macros", user_attribute_macros)
        if user_attribute_mappings is not None:
            pulumi.set(__self__, "user_attribute_mappings", user_attribute_mappings)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="paramKeyName")
    def param_key_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "param_key_name")

    @param_key_name.setter
    def param_key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "param_key_name", value)

    @property
    @pulumi.getter(name="attributesTransformations")
    def attributes_transformations(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "attributes_transformations")

    @attributes_transformations.setter
    def attributes_transformations(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attributes_transformations", value)

    @property
    @pulumi.getter(name="defaultValues")
    def default_values(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_values")

    @default_values.setter
    def default_values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_values", value)

    @property
    @pulumi.getter(name="includeInSamlAssertion")
    def include_in_saml_assertion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "include_in_saml_assertion")

    @include_in_saml_assertion.setter
    def include_in_saml_assertion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_in_saml_assertion", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="paramId")
    def param_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "param_id")

    @param_id.setter
    def param_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "param_id", value)

    @property
    @pulumi.getter(name="provisionedEntitlements")
    def provisioned_entitlements(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "provisioned_entitlements")

    @provisioned_entitlements.setter
    def provisioned_entitlements(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "provisioned_entitlements", value)

    @property
    @pulumi.getter(name="safeEntitlementsEnabled")
    def safe_entitlements_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "safe_entitlements_enabled")

    @safe_entitlements_enabled.setter
    def safe_entitlements_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "safe_entitlements_enabled", value)

    @property
    @pulumi.getter(name="skipIfBlank")
    def skip_if_blank(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_if_blank")

    @skip_if_blank.setter
    def skip_if_blank(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_if_blank", value)

    @property
    @pulumi.getter(name="userAttributeMacros")
    def user_attribute_macros(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_attribute_macros")

    @user_attribute_macros.setter
    def user_attribute_macros(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute_macros", value)

    @property
    @pulumi.getter(name="userAttributeMappings")
    def user_attribute_mappings(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_attribute_mappings")

    @user_attribute_mappings.setter
    def user_attribute_mappings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute_mappings", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class PrivilegesPrivilegeArgs:
    def __init__(__self__, *,
                 statements: pulumi.Input[Sequence[pulumi.Input['PrivilegesPrivilegeStatementArgs']]],
                 version: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "statements", statements)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def statements(self) -> pulumi.Input[Sequence[pulumi.Input['PrivilegesPrivilegeStatementArgs']]]:
        return pulumi.get(self, "statements")

    @statements.setter
    def statements(self, value: pulumi.Input[Sequence[pulumi.Input['PrivilegesPrivilegeStatementArgs']]]):
        pulumi.set(self, "statements", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class PrivilegesPrivilegeStatementArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input[str]]],
                 effect: pulumi.Input[str],
                 scopes: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "effect", effect)
        pulumi.set(__self__, "scopes", scopes)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def effect(self) -> pulumi.Input[str]:
        return pulumi.get(self, "effect")

    @effect.setter
    def effect(self, value: pulumi.Input[str]):
        pulumi.set(self, "effect", value)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scopes", value)


@pulumi.input_type
class SamlAppParameterArgs:
    def __init__(__self__, *,
                 param_key_name: pulumi.Input[str],
                 attributes_transformations: Optional[pulumi.Input[str]] = None,
                 default_values: Optional[pulumi.Input[str]] = None,
                 include_in_saml_assertion: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 param_id: Optional[pulumi.Input[int]] = None,
                 provisioned_entitlements: Optional[pulumi.Input[bool]] = None,
                 safe_entitlements_enabled: Optional[pulumi.Input[bool]] = None,
                 skip_if_blank: Optional[pulumi.Input[bool]] = None,
                 user_attribute_macros: Optional[pulumi.Input[str]] = None,
                 user_attribute_mappings: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "param_key_name", param_key_name)
        if attributes_transformations is not None:
            pulumi.set(__self__, "attributes_transformations", attributes_transformations)
        if default_values is not None:
            pulumi.set(__self__, "default_values", default_values)
        if include_in_saml_assertion is not None:
            pulumi.set(__self__, "include_in_saml_assertion", include_in_saml_assertion)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if param_id is not None:
            pulumi.set(__self__, "param_id", param_id)
        if provisioned_entitlements is not None:
            pulumi.set(__self__, "provisioned_entitlements", provisioned_entitlements)
        if safe_entitlements_enabled is not None:
            pulumi.set(__self__, "safe_entitlements_enabled", safe_entitlements_enabled)
        if skip_if_blank is not None:
            pulumi.set(__self__, "skip_if_blank", skip_if_blank)
        if user_attribute_macros is not None:
            pulumi.set(__self__, "user_attribute_macros", user_attribute_macros)
        if user_attribute_mappings is not None:
            pulumi.set(__self__, "user_attribute_mappings", user_attribute_mappings)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="paramKeyName")
    def param_key_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "param_key_name")

    @param_key_name.setter
    def param_key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "param_key_name", value)

    @property
    @pulumi.getter(name="attributesTransformations")
    def attributes_transformations(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "attributes_transformations")

    @attributes_transformations.setter
    def attributes_transformations(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attributes_transformations", value)

    @property
    @pulumi.getter(name="defaultValues")
    def default_values(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_values")

    @default_values.setter
    def default_values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_values", value)

    @property
    @pulumi.getter(name="includeInSamlAssertion")
    def include_in_saml_assertion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "include_in_saml_assertion")

    @include_in_saml_assertion.setter
    def include_in_saml_assertion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_in_saml_assertion", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="paramId")
    def param_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "param_id")

    @param_id.setter
    def param_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "param_id", value)

    @property
    @pulumi.getter(name="provisionedEntitlements")
    def provisioned_entitlements(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "provisioned_entitlements")

    @provisioned_entitlements.setter
    def provisioned_entitlements(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "provisioned_entitlements", value)

    @property
    @pulumi.getter(name="safeEntitlementsEnabled")
    def safe_entitlements_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "safe_entitlements_enabled")

    @safe_entitlements_enabled.setter
    def safe_entitlements_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "safe_entitlements_enabled", value)

    @property
    @pulumi.getter(name="skipIfBlank")
    def skip_if_blank(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_if_blank")

    @skip_if_blank.setter
    def skip_if_blank(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_if_blank", value)

    @property
    @pulumi.getter(name="userAttributeMacros")
    def user_attribute_macros(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_attribute_macros")

    @user_attribute_macros.setter
    def user_attribute_macros(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute_macros", value)

    @property
    @pulumi.getter(name="userAttributeMappings")
    def user_attribute_mappings(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_attribute_mappings")

    @user_attribute_mappings.setter
    def user_attribute_mappings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute_mappings", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class SmartHookConditionArgs:
    def __init__(__self__, *,
                 operator: pulumi.Input[str],
                 source: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[str]:
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[str]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class SmartHookOptionsArgs:
    def __init__(__self__, *,
                 location_enabled: Optional[pulumi.Input[bool]] = None,
                 mfa_device_info_enabled: Optional[pulumi.Input[bool]] = None,
                 risk_enabled: Optional[pulumi.Input[bool]] = None):
        if location_enabled is not None:
            pulumi.set(__self__, "location_enabled", location_enabled)
        if mfa_device_info_enabled is not None:
            pulumi.set(__self__, "mfa_device_info_enabled", mfa_device_info_enabled)
        if risk_enabled is not None:
            pulumi.set(__self__, "risk_enabled", risk_enabled)

    @property
    @pulumi.getter(name="locationEnabled")
    def location_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "location_enabled")

    @location_enabled.setter
    def location_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "location_enabled", value)

    @property
    @pulumi.getter(name="mfaDeviceInfoEnabled")
    def mfa_device_info_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "mfa_device_info_enabled")

    @mfa_device_info_enabled.setter
    def mfa_device_info_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mfa_device_info_enabled", value)

    @property
    @pulumi.getter(name="riskEnabled")
    def risk_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "risk_enabled")

    @risk_enabled.setter
    def risk_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "risk_enabled", value)


@pulumi.input_type
class UserMappingActionArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class UserMappingConditionArgs:
    def __init__(__self__, *,
                 operator: pulumi.Input[str],
                 source: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[str]:
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[str]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


