# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetUsersResult',
    'AwaitableGetUsersResult',
    'get_users',
]

@pulumi.output_type
class GetUsersResult:
    """
    A collection of values returned by getUsers.
    """
    def __init__(__self__, directory_id=None, external_id=None, firstname=None, id=None, ids=None, lastname=None, samaccountname=None, user_id=None, username=None):
        if directory_id and not isinstance(directory_id, int):
            raise TypeError("Expected argument 'directory_id' to be a int")
        pulumi.set(__self__, "directory_id", directory_id)
        if external_id and not isinstance(external_id, int):
            raise TypeError("Expected argument 'external_id' to be a int")
        pulumi.set(__self__, "external_id", external_id)
        if firstname and not isinstance(firstname, str):
            raise TypeError("Expected argument 'firstname' to be a str")
        pulumi.set(__self__, "firstname", firstname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if lastname and not isinstance(lastname, str):
            raise TypeError("Expected argument 'lastname' to be a str")
        pulumi.set(__self__, "lastname", lastname)
        if samaccountname and not isinstance(samaccountname, str):
            raise TypeError("Expected argument 'samaccountname' to be a str")
        pulumi.set(__self__, "samaccountname", samaccountname)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[int]:
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[int]:
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def firstname(self) -> Optional[str]:
        return pulumi.get(self, "firstname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def lastname(self) -> Optional[str]:
        return pulumi.get(self, "lastname")

    @property
    @pulumi.getter
    def samaccountname(self) -> Optional[str]:
        return pulumi.get(self, "samaccountname")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[str]:
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        return pulumi.get(self, "username")


class AwaitableGetUsersResult(GetUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsersResult(
            directory_id=self.directory_id,
            external_id=self.external_id,
            firstname=self.firstname,
            id=self.id,
            ids=self.ids,
            lastname=self.lastname,
            samaccountname=self.samaccountname,
            user_id=self.user_id,
            username=self.username)


def get_users(directory_id: Optional[int] = None,
              external_id: Optional[int] = None,
              firstname: Optional[str] = None,
              lastname: Optional[str] = None,
              samaccountname: Optional[str] = None,
              user_id: Optional[str] = None,
              username: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUsersResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['directoryId'] = directory_id
    __args__['externalId'] = external_id
    __args__['firstname'] = firstname
    __args__['lastname'] = lastname
    __args__['samaccountname'] = samaccountname
    __args__['userId'] = user_id
    __args__['username'] = username
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('onelogin:index/getUsers:getUsers', __args__, opts=opts, typ=GetUsersResult).value

    return AwaitableGetUsersResult(
        directory_id=__ret__.directory_id,
        external_id=__ret__.external_id,
        firstname=__ret__.firstname,
        id=__ret__.id,
        ids=__ret__.ids,
        lastname=__ret__.lastname,
        samaccountname=__ret__.samaccountname,
        user_id=__ret__.user_id,
        username=__ret__.username)
