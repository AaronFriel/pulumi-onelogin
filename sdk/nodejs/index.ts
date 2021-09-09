// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./app";
export * from "./appRoleAttachment";
export * from "./appRule";
export * from "./getUser";
export * from "./getUsers";
export * from "./oidcApp";
export * from "./privileges";
export * from "./provider";
export * from "./role";
export * from "./samlApp";
export * from "./smartHook";
export * from "./user";
export * from "./userMapping";

// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

// Import resources to register:
import { App } from "./app";
import { AppRoleAttachment } from "./appRoleAttachment";
import { AppRule } from "./appRule";
import { OidcApp } from "./oidcApp";
import { Privileges } from "./privileges";
import { Role } from "./role";
import { SamlApp } from "./samlApp";
import { SmartHook } from "./smartHook";
import { User } from "./user";
import { UserMapping } from "./userMapping";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "onelogin:index/app:App":
                return new App(name, <any>undefined, { urn })
            case "onelogin:index/appRoleAttachment:AppRoleAttachment":
                return new AppRoleAttachment(name, <any>undefined, { urn })
            case "onelogin:index/appRule:AppRule":
                return new AppRule(name, <any>undefined, { urn })
            case "onelogin:index/oidcApp:OidcApp":
                return new OidcApp(name, <any>undefined, { urn })
            case "onelogin:index/privileges:Privileges":
                return new Privileges(name, <any>undefined, { urn })
            case "onelogin:index/role:Role":
                return new Role(name, <any>undefined, { urn })
            case "onelogin:index/samlApp:SamlApp":
                return new SamlApp(name, <any>undefined, { urn })
            case "onelogin:index/smartHook:SmartHook":
                return new SmartHook(name, <any>undefined, { urn })
            case "onelogin:index/user:User":
                return new User(name, <any>undefined, { urn })
            case "onelogin:index/userMapping:UserMapping":
                return new UserMapping(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("onelogin", "index/app", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/appRoleAttachment", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/appRule", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/oidcApp", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/privileges", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/role", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/samlApp", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/smartHook", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/user", _module)
pulumi.runtime.registerResourceModule("onelogin", "index/userMapping", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("onelogin", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:onelogin") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
