// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onelogin
{
    [OneloginResourceType("onelogin:index/appRoleAttachment:AppRoleAttachment")]
    public partial class AppRoleAttachment : Pulumi.CustomResource
    {
        [Output("appId")]
        public Output<int> AppId { get; private set; } = null!;

        [Output("roleId")]
        public Output<int> RoleId { get; private set; } = null!;


        /// <summary>
        /// Create a AppRoleAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AppRoleAttachment(string name, AppRoleAttachmentArgs args, CustomResourceOptions? options = null)
            : base("onelogin:index/appRoleAttachment:AppRoleAttachment", name, args ?? new AppRoleAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AppRoleAttachment(string name, Input<string> id, AppRoleAttachmentState? state = null, CustomResourceOptions? options = null)
            : base("onelogin:index/appRoleAttachment:AppRoleAttachment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AppRoleAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AppRoleAttachment Get(string name, Input<string> id, AppRoleAttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new AppRoleAttachment(name, id, state, options);
        }
    }

    public sealed class AppRoleAttachmentArgs : Pulumi.ResourceArgs
    {
        [Input("appId", required: true)]
        public Input<int> AppId { get; set; } = null!;

        [Input("roleId", required: true)]
        public Input<int> RoleId { get; set; } = null!;

        public AppRoleAttachmentArgs()
        {
        }
    }

    public sealed class AppRoleAttachmentState : Pulumi.ResourceArgs
    {
        [Input("appId")]
        public Input<int>? AppId { get; set; }

        [Input("roleId")]
        public Input<int>? RoleId { get; set; }

        public AppRoleAttachmentState()
        {
        }
    }
}
