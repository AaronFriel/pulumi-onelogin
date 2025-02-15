# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SamlAppArgs', 'SamlApp']

@pulumi.input_type
class SamlAppArgs:
    def __init__(__self__, *,
                 connector_id: pulumi.Input[int],
                 allow_assumed_signin: Optional[pulumi.Input[bool]] = None,
                 brand_id: Optional[pulumi.Input[int]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['SamlAppParameterArgs']]]] = None,
                 provisioning: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]] = None,
                 visible: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a SamlApp resource.
        """
        pulumi.set(__self__, "connector_id", connector_id)
        if allow_assumed_signin is not None:
            pulumi.set(__self__, "allow_assumed_signin", allow_assumed_signin)
        if brand_id is not None:
            pulumi.set(__self__, "brand_id", brand_id)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if provisioning is not None:
            pulumi.set(__self__, "provisioning", provisioning)
        if visible is not None:
            pulumi.set(__self__, "visible", visible)

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "connector_id")

    @connector_id.setter
    def connector_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "connector_id", value)

    @property
    @pulumi.getter(name="allowAssumedSignin")
    def allow_assumed_signin(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_assumed_signin")

    @allow_assumed_signin.setter
    def allow_assumed_signin(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_assumed_signin", value)

    @property
    @pulumi.getter(name="brandId")
    def brand_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "brand_id")

    @brand_id.setter
    def brand_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "brand_id", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SamlAppParameterArgs']]]]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SamlAppParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def provisioning(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]]:
        return pulumi.get(self, "provisioning")

    @provisioning.setter
    def provisioning(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]]):
        pulumi.set(self, "provisioning", value)

    @property
    @pulumi.getter
    def visible(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "visible")

    @visible.setter
    def visible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "visible", value)


@pulumi.input_type
class _SamlAppState:
    def __init__(__self__, *,
                 allow_assumed_signin: Optional[pulumi.Input[bool]] = None,
                 auth_method: Optional[pulumi.Input[int]] = None,
                 brand_id: Optional[pulumi.Input[int]] = None,
                 certificate: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 connector_id: Optional[pulumi.Input[int]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['SamlAppParameterArgs']]]] = None,
                 policy_id: Optional[pulumi.Input[int]] = None,
                 provisioning: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]] = None,
                 sso: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tab_id: Optional[pulumi.Input[int]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 visible: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering SamlApp resources.
        """
        if allow_assumed_signin is not None:
            pulumi.set(__self__, "allow_assumed_signin", allow_assumed_signin)
        if auth_method is not None:
            pulumi.set(__self__, "auth_method", auth_method)
        if brand_id is not None:
            pulumi.set(__self__, "brand_id", brand_id)
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if connector_id is not None:
            pulumi.set(__self__, "connector_id", connector_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_url is not None:
            pulumi.set(__self__, "icon_url", icon_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if provisioning is not None:
            pulumi.set(__self__, "provisioning", provisioning)
        if sso is not None:
            pulumi.set(__self__, "sso", sso)
        if tab_id is not None:
            pulumi.set(__self__, "tab_id", tab_id)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if visible is not None:
            pulumi.set(__self__, "visible", visible)

    @property
    @pulumi.getter(name="allowAssumedSignin")
    def allow_assumed_signin(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_assumed_signin")

    @allow_assumed_signin.setter
    def allow_assumed_signin(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_assumed_signin", value)

    @property
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "auth_method")

    @auth_method.setter
    def auth_method(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "auth_method", value)

    @property
    @pulumi.getter(name="brandId")
    def brand_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "brand_id")

    @brand_id.setter
    def brand_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "brand_id", value)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "connector_id")

    @connector_id.setter
    def connector_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "connector_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "icon_url")

    @icon_url.setter
    def icon_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SamlAppParameterArgs']]]]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SamlAppParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter
    def provisioning(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]]:
        return pulumi.get(self, "provisioning")

    @provisioning.setter
    def provisioning(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]]):
        pulumi.set(self, "provisioning", value)

    @property
    @pulumi.getter
    def sso(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "sso")

    @sso.setter
    def sso(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "sso", value)

    @property
    @pulumi.getter(name="tabId")
    def tab_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "tab_id")

    @tab_id.setter
    def tab_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tab_id", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter
    def visible(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "visible")

    @visible.setter
    def visible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "visible", value)


class SamlApp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_assumed_signin: Optional[pulumi.Input[bool]] = None,
                 brand_id: Optional[pulumi.Input[int]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 connector_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SamlAppParameterArgs']]]]] = None,
                 provisioning: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]] = None,
                 visible: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a SamlApp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SamlAppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SamlApp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SamlAppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SamlAppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_assumed_signin: Optional[pulumi.Input[bool]] = None,
                 brand_id: Optional[pulumi.Input[int]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 connector_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SamlAppParameterArgs']]]]] = None,
                 provisioning: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]] = None,
                 visible: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SamlAppArgs.__new__(SamlAppArgs)

            __props__.__dict__["allow_assumed_signin"] = allow_assumed_signin
            __props__.__dict__["brand_id"] = brand_id
            __props__.__dict__["configuration"] = configuration
            if connector_id is None and not opts.urn:
                raise TypeError("Missing required property 'connector_id'")
            __props__.__dict__["connector_id"] = connector_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["notes"] = notes
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["provisioning"] = provisioning
            __props__.__dict__["visible"] = visible
            __props__.__dict__["auth_method"] = None
            __props__.__dict__["certificate"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["icon_url"] = None
            __props__.__dict__["policy_id"] = None
            __props__.__dict__["sso"] = None
            __props__.__dict__["tab_id"] = None
            __props__.__dict__["updated_at"] = None
        super(SamlApp, __self__).__init__(
            'onelogin:index/samlApp:SamlApp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_assumed_signin: Optional[pulumi.Input[bool]] = None,
            auth_method: Optional[pulumi.Input[int]] = None,
            brand_id: Optional[pulumi.Input[int]] = None,
            certificate: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            connector_id: Optional[pulumi.Input[int]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            icon_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notes: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SamlAppParameterArgs']]]]] = None,
            policy_id: Optional[pulumi.Input[int]] = None,
            provisioning: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]] = None,
            sso: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tab_id: Optional[pulumi.Input[int]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            visible: Optional[pulumi.Input[bool]] = None) -> 'SamlApp':
        """
        Get an existing SamlApp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SamlAppState.__new__(_SamlAppState)

        __props__.__dict__["allow_assumed_signin"] = allow_assumed_signin
        __props__.__dict__["auth_method"] = auth_method
        __props__.__dict__["brand_id"] = brand_id
        __props__.__dict__["certificate"] = certificate
        __props__.__dict__["configuration"] = configuration
        __props__.__dict__["connector_id"] = connector_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["icon_url"] = icon_url
        __props__.__dict__["name"] = name
        __props__.__dict__["notes"] = notes
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["policy_id"] = policy_id
        __props__.__dict__["provisioning"] = provisioning
        __props__.__dict__["sso"] = sso
        __props__.__dict__["tab_id"] = tab_id
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["visible"] = visible
        return SamlApp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowAssumedSignin")
    def allow_assumed_signin(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_assumed_signin")

    @property
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> pulumi.Output[int]:
        return pulumi.get(self, "auth_method")

    @property
    @pulumi.getter(name="brandId")
    def brand_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "brand_id")

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "connector_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "icon_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Sequence['outputs.SamlAppParameter']]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def provisioning(self) -> pulumi.Output[Mapping[str, bool]]:
        return pulumi.get(self, "provisioning")

    @property
    @pulumi.getter
    def sso(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "sso")

    @property
    @pulumi.getter(name="tabId")
    def tab_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "tab_id")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def visible(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "visible")

