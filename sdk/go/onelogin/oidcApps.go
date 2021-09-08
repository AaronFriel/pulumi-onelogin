// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package onelogin

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type OidcApps struct {
	pulumi.CustomResourceState

	AllowAssumedSignin pulumi.BoolPtrOutput         `pulumi:"allowAssumedSignin"`
	AuthMethod         pulumi.IntOutput             `pulumi:"authMethod"`
	BrandId            pulumi.IntPtrOutput          `pulumi:"brandId"`
	Configuration      pulumi.StringMapOutput       `pulumi:"configuration"`
	ConnectorId        pulumi.IntOutput             `pulumi:"connectorId"`
	CreatedAt          pulumi.StringOutput          `pulumi:"createdAt"`
	Description        pulumi.StringPtrOutput       `pulumi:"description"`
	IconUrl            pulumi.StringOutput          `pulumi:"iconUrl"`
	Name               pulumi.StringOutput          `pulumi:"name"`
	Notes              pulumi.StringPtrOutput       `pulumi:"notes"`
	Parameters         OidcAppsParameterArrayOutput `pulumi:"parameters"`
	PolicyId           pulumi.IntOutput             `pulumi:"policyId"`
	Provisioning       pulumi.BoolMapOutput         `pulumi:"provisioning"`
	Sso                pulumi.StringMapOutput       `pulumi:"sso"`
	TabId              pulumi.IntOutput             `pulumi:"tabId"`
	UpdatedAt          pulumi.StringOutput          `pulumi:"updatedAt"`
	Visible            pulumi.BoolPtrOutput         `pulumi:"visible"`
}

// NewOidcApps registers a new resource with the given unique name, arguments, and options.
func NewOidcApps(ctx *pulumi.Context,
	name string, args *OidcAppsArgs, opts ...pulumi.ResourceOption) (*OidcApps, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectorId == nil {
		return nil, errors.New("invalid value for required argument 'ConnectorId'")
	}
	var resource OidcApps
	err := ctx.RegisterResource("onelogin:index/oidcApps:OidcApps", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOidcApps gets an existing OidcApps resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOidcApps(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OidcAppsState, opts ...pulumi.ResourceOption) (*OidcApps, error) {
	var resource OidcApps
	err := ctx.ReadResource("onelogin:index/oidcApps:OidcApps", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OidcApps resources.
type oidcAppsState struct {
	AllowAssumedSignin *bool               `pulumi:"allowAssumedSignin"`
	AuthMethod         *int                `pulumi:"authMethod"`
	BrandId            *int                `pulumi:"brandId"`
	Configuration      map[string]string   `pulumi:"configuration"`
	ConnectorId        *int                `pulumi:"connectorId"`
	CreatedAt          *string             `pulumi:"createdAt"`
	Description        *string             `pulumi:"description"`
	IconUrl            *string             `pulumi:"iconUrl"`
	Name               *string             `pulumi:"name"`
	Notes              *string             `pulumi:"notes"`
	Parameters         []OidcAppsParameter `pulumi:"parameters"`
	PolicyId           *int                `pulumi:"policyId"`
	Provisioning       map[string]bool     `pulumi:"provisioning"`
	Sso                map[string]string   `pulumi:"sso"`
	TabId              *int                `pulumi:"tabId"`
	UpdatedAt          *string             `pulumi:"updatedAt"`
	Visible            *bool               `pulumi:"visible"`
}

type OidcAppsState struct {
	AllowAssumedSignin pulumi.BoolPtrInput
	AuthMethod         pulumi.IntPtrInput
	BrandId            pulumi.IntPtrInput
	Configuration      pulumi.StringMapInput
	ConnectorId        pulumi.IntPtrInput
	CreatedAt          pulumi.StringPtrInput
	Description        pulumi.StringPtrInput
	IconUrl            pulumi.StringPtrInput
	Name               pulumi.StringPtrInput
	Notes              pulumi.StringPtrInput
	Parameters         OidcAppsParameterArrayInput
	PolicyId           pulumi.IntPtrInput
	Provisioning       pulumi.BoolMapInput
	Sso                pulumi.StringMapInput
	TabId              pulumi.IntPtrInput
	UpdatedAt          pulumi.StringPtrInput
	Visible            pulumi.BoolPtrInput
}

func (OidcAppsState) ElementType() reflect.Type {
	return reflect.TypeOf((*oidcAppsState)(nil)).Elem()
}

type oidcAppsArgs struct {
	AllowAssumedSignin *bool               `pulumi:"allowAssumedSignin"`
	BrandId            *int                `pulumi:"brandId"`
	Configuration      map[string]string   `pulumi:"configuration"`
	ConnectorId        int                 `pulumi:"connectorId"`
	Description        *string             `pulumi:"description"`
	Name               *string             `pulumi:"name"`
	Notes              *string             `pulumi:"notes"`
	Parameters         []OidcAppsParameter `pulumi:"parameters"`
	Provisioning       map[string]bool     `pulumi:"provisioning"`
	Visible            *bool               `pulumi:"visible"`
}

// The set of arguments for constructing a OidcApps resource.
type OidcAppsArgs struct {
	AllowAssumedSignin pulumi.BoolPtrInput
	BrandId            pulumi.IntPtrInput
	Configuration      pulumi.StringMapInput
	ConnectorId        pulumi.IntInput
	Description        pulumi.StringPtrInput
	Name               pulumi.StringPtrInput
	Notes              pulumi.StringPtrInput
	Parameters         OidcAppsParameterArrayInput
	Provisioning       pulumi.BoolMapInput
	Visible            pulumi.BoolPtrInput
}

func (OidcAppsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*oidcAppsArgs)(nil)).Elem()
}

type OidcAppsInput interface {
	pulumi.Input

	ToOidcAppsOutput() OidcAppsOutput
	ToOidcAppsOutputWithContext(ctx context.Context) OidcAppsOutput
}

func (*OidcApps) ElementType() reflect.Type {
	return reflect.TypeOf((*OidcApps)(nil))
}

func (i *OidcApps) ToOidcAppsOutput() OidcAppsOutput {
	return i.ToOidcAppsOutputWithContext(context.Background())
}

func (i *OidcApps) ToOidcAppsOutputWithContext(ctx context.Context) OidcAppsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OidcAppsOutput)
}

func (i *OidcApps) ToOidcAppsPtrOutput() OidcAppsPtrOutput {
	return i.ToOidcAppsPtrOutputWithContext(context.Background())
}

func (i *OidcApps) ToOidcAppsPtrOutputWithContext(ctx context.Context) OidcAppsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OidcAppsPtrOutput)
}

type OidcAppsPtrInput interface {
	pulumi.Input

	ToOidcAppsPtrOutput() OidcAppsPtrOutput
	ToOidcAppsPtrOutputWithContext(ctx context.Context) OidcAppsPtrOutput
}

type oidcAppsPtrType OidcAppsArgs

func (*oidcAppsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**OidcApps)(nil))
}

func (i *oidcAppsPtrType) ToOidcAppsPtrOutput() OidcAppsPtrOutput {
	return i.ToOidcAppsPtrOutputWithContext(context.Background())
}

func (i *oidcAppsPtrType) ToOidcAppsPtrOutputWithContext(ctx context.Context) OidcAppsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OidcAppsPtrOutput)
}

// OidcAppsArrayInput is an input type that accepts OidcAppsArray and OidcAppsArrayOutput values.
// You can construct a concrete instance of `OidcAppsArrayInput` via:
//
//          OidcAppsArray{ OidcAppsArgs{...} }
type OidcAppsArrayInput interface {
	pulumi.Input

	ToOidcAppsArrayOutput() OidcAppsArrayOutput
	ToOidcAppsArrayOutputWithContext(context.Context) OidcAppsArrayOutput
}

type OidcAppsArray []OidcAppsInput

func (OidcAppsArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*OidcApps)(nil))
}

func (i OidcAppsArray) ToOidcAppsArrayOutput() OidcAppsArrayOutput {
	return i.ToOidcAppsArrayOutputWithContext(context.Background())
}

func (i OidcAppsArray) ToOidcAppsArrayOutputWithContext(ctx context.Context) OidcAppsArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OidcAppsArrayOutput)
}

// OidcAppsMapInput is an input type that accepts OidcAppsMap and OidcAppsMapOutput values.
// You can construct a concrete instance of `OidcAppsMapInput` via:
//
//          OidcAppsMap{ "key": OidcAppsArgs{...} }
type OidcAppsMapInput interface {
	pulumi.Input

	ToOidcAppsMapOutput() OidcAppsMapOutput
	ToOidcAppsMapOutputWithContext(context.Context) OidcAppsMapOutput
}

type OidcAppsMap map[string]OidcAppsInput

func (OidcAppsMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*OidcApps)(nil))
}

func (i OidcAppsMap) ToOidcAppsMapOutput() OidcAppsMapOutput {
	return i.ToOidcAppsMapOutputWithContext(context.Background())
}

func (i OidcAppsMap) ToOidcAppsMapOutputWithContext(ctx context.Context) OidcAppsMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OidcAppsMapOutput)
}

type OidcAppsOutput struct {
	*pulumi.OutputState
}

func (OidcAppsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*OidcApps)(nil))
}

func (o OidcAppsOutput) ToOidcAppsOutput() OidcAppsOutput {
	return o
}

func (o OidcAppsOutput) ToOidcAppsOutputWithContext(ctx context.Context) OidcAppsOutput {
	return o
}

func (o OidcAppsOutput) ToOidcAppsPtrOutput() OidcAppsPtrOutput {
	return o.ToOidcAppsPtrOutputWithContext(context.Background())
}

func (o OidcAppsOutput) ToOidcAppsPtrOutputWithContext(ctx context.Context) OidcAppsPtrOutput {
	return o.ApplyT(func(v OidcApps) *OidcApps {
		return &v
	}).(OidcAppsPtrOutput)
}

type OidcAppsPtrOutput struct {
	*pulumi.OutputState
}

func (OidcAppsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OidcApps)(nil))
}

func (o OidcAppsPtrOutput) ToOidcAppsPtrOutput() OidcAppsPtrOutput {
	return o
}

func (o OidcAppsPtrOutput) ToOidcAppsPtrOutputWithContext(ctx context.Context) OidcAppsPtrOutput {
	return o
}

type OidcAppsArrayOutput struct{ *pulumi.OutputState }

func (OidcAppsArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]OidcApps)(nil))
}

func (o OidcAppsArrayOutput) ToOidcAppsArrayOutput() OidcAppsArrayOutput {
	return o
}

func (o OidcAppsArrayOutput) ToOidcAppsArrayOutputWithContext(ctx context.Context) OidcAppsArrayOutput {
	return o
}

func (o OidcAppsArrayOutput) Index(i pulumi.IntInput) OidcAppsOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) OidcApps {
		return vs[0].([]OidcApps)[vs[1].(int)]
	}).(OidcAppsOutput)
}

type OidcAppsMapOutput struct{ *pulumi.OutputState }

func (OidcAppsMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]OidcApps)(nil))
}

func (o OidcAppsMapOutput) ToOidcAppsMapOutput() OidcAppsMapOutput {
	return o
}

func (o OidcAppsMapOutput) ToOidcAppsMapOutputWithContext(ctx context.Context) OidcAppsMapOutput {
	return o
}

func (o OidcAppsMapOutput) MapIndex(k pulumi.StringInput) OidcAppsOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) OidcApps {
		return vs[0].(map[string]OidcApps)[vs[1].(string)]
	}).(OidcAppsOutput)
}

func init() {
	pulumi.RegisterOutputType(OidcAppsOutput{})
	pulumi.RegisterOutputType(OidcAppsPtrOutput{})
	pulumi.RegisterOutputType(OidcAppsArrayOutput{})
	pulumi.RegisterOutputType(OidcAppsMapOutput{})
}
