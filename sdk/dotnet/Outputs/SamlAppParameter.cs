// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onelogin.Outputs
{

    [OutputType]
    public sealed class SamlAppParameter
    {
        public readonly string? AttributesTransformations;
        public readonly string? DefaultValues;
        public readonly bool? IncludeInSamlAssertion;
        public readonly string? Label;
        public readonly int? ParamId;
        public readonly string ParamKeyName;
        public readonly bool? ProvisionedEntitlements;
        public readonly bool? SafeEntitlementsEnabled;
        public readonly bool? SkipIfBlank;
        public readonly string? UserAttributeMacros;
        public readonly string? UserAttributeMappings;
        public readonly string? Values;

        [OutputConstructor]
        private SamlAppParameter(
            string? attributesTransformations,

            string? defaultValues,

            bool? includeInSamlAssertion,

            string? label,

            int? paramId,

            string paramKeyName,

            bool? provisionedEntitlements,

            bool? safeEntitlementsEnabled,

            bool? skipIfBlank,

            string? userAttributeMacros,

            string? userAttributeMappings,

            string? values)
        {
            AttributesTransformations = attributesTransformations;
            DefaultValues = defaultValues;
            IncludeInSamlAssertion = includeInSamlAssertion;
            Label = label;
            ParamId = paramId;
            ParamKeyName = paramKeyName;
            ProvisionedEntitlements = provisionedEntitlements;
            SafeEntitlementsEnabled = safeEntitlementsEnabled;
            SkipIfBlank = skipIfBlank;
            UserAttributeMacros = userAttributeMacros;
            UserAttributeMappings = userAttributeMappings;
            Values = values;
        }
    }
}
