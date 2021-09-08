// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package onelogin

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type App struct {
	pulumi.CustomResourceState

	AllowAssumedSignin pulumi.BoolPtrOutput    `pulumi:"allowAssumedSignin"`
	AuthMethod         pulumi.IntOutput        `pulumi:"authMethod"`
	BrandId            pulumi.IntPtrOutput     `pulumi:"brandId"`
	ConnectorId        pulumi.IntOutput        `pulumi:"connectorId"`
	CreatedAt          pulumi.StringOutput     `pulumi:"createdAt"`
	Description        pulumi.StringPtrOutput  `pulumi:"description"`
	IconUrl            pulumi.StringOutput     `pulumi:"iconUrl"`
	Name               pulumi.StringOutput     `pulumi:"name"`
	Notes              pulumi.StringPtrOutput  `pulumi:"notes"`
	Parameters         AppParameterArrayOutput `pulumi:"parameters"`
	PolicyId           pulumi.IntOutput        `pulumi:"policyId"`
	Provisioning       pulumi.BoolMapOutput    `pulumi:"provisioning"`
	TabId              pulumi.IntOutput        `pulumi:"tabId"`
	UpdatedAt          pulumi.StringOutput     `pulumi:"updatedAt"`
	Visible            pulumi.BoolPtrOutput    `pulumi:"visible"`
}

// NewApp registers a new resource with the given unique name, arguments, and options.
func NewApp(ctx *pulumi.Context,
	name string, args *AppArgs, opts ...pulumi.ResourceOption) (*App, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectorId == nil {
		return nil, errors.New("invalid value for required argument 'ConnectorId'")
	}
	var resource App
	err := ctx.RegisterResource("onelogin:index/app:App", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApp gets an existing App resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApp(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AppState, opts ...pulumi.ResourceOption) (*App, error) {
	var resource App
	err := ctx.ReadResource("onelogin:index/app:App", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering App resources.
type appState struct {
	AllowAssumedSignin *bool           `pulumi:"allowAssumedSignin"`
	AuthMethod         *int            `pulumi:"authMethod"`
	BrandId            *int            `pulumi:"brandId"`
	ConnectorId        *int            `pulumi:"connectorId"`
	CreatedAt          *string         `pulumi:"createdAt"`
	Description        *string         `pulumi:"description"`
	IconUrl            *string         `pulumi:"iconUrl"`
	Name               *string         `pulumi:"name"`
	Notes              *string         `pulumi:"notes"`
	Parameters         []AppParameter  `pulumi:"parameters"`
	PolicyId           *int            `pulumi:"policyId"`
	Provisioning       map[string]bool `pulumi:"provisioning"`
	TabId              *int            `pulumi:"tabId"`
	UpdatedAt          *string         `pulumi:"updatedAt"`
	Visible            *bool           `pulumi:"visible"`
}

type AppState struct {
	AllowAssumedSignin pulumi.BoolPtrInput
	AuthMethod         pulumi.IntPtrInput
	BrandId            pulumi.IntPtrInput
	ConnectorId        pulumi.IntPtrInput
	CreatedAt          pulumi.StringPtrInput
	Description        pulumi.StringPtrInput
	IconUrl            pulumi.StringPtrInput
	Name               pulumi.StringPtrInput
	Notes              pulumi.StringPtrInput
	Parameters         AppParameterArrayInput
	PolicyId           pulumi.IntPtrInput
	Provisioning       pulumi.BoolMapInput
	TabId              pulumi.IntPtrInput
	UpdatedAt          pulumi.StringPtrInput
	Visible            pulumi.BoolPtrInput
}

func (AppState) ElementType() reflect.Type {
	return reflect.TypeOf((*appState)(nil)).Elem()
}

type appArgs struct {
	AllowAssumedSignin *bool           `pulumi:"allowAssumedSignin"`
	BrandId            *int            `pulumi:"brandId"`
	ConnectorId        int             `pulumi:"connectorId"`
	Description        *string         `pulumi:"description"`
	Name               *string         `pulumi:"name"`
	Notes              *string         `pulumi:"notes"`
	Parameters         []AppParameter  `pulumi:"parameters"`
	Provisioning       map[string]bool `pulumi:"provisioning"`
	Visible            *bool           `pulumi:"visible"`
}

// The set of arguments for constructing a App resource.
type AppArgs struct {
	AllowAssumedSignin pulumi.BoolPtrInput
	BrandId            pulumi.IntPtrInput
	ConnectorId        pulumi.IntInput
	Description        pulumi.StringPtrInput
	Name               pulumi.StringPtrInput
	Notes              pulumi.StringPtrInput
	Parameters         AppParameterArrayInput
	Provisioning       pulumi.BoolMapInput
	Visible            pulumi.BoolPtrInput
}

func (AppArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*appArgs)(nil)).Elem()
}

type AppInput interface {
	pulumi.Input

	ToAppOutput() AppOutput
	ToAppOutputWithContext(ctx context.Context) AppOutput
}

func (*App) ElementType() reflect.Type {
	return reflect.TypeOf((*App)(nil))
}

func (i *App) ToAppOutput() AppOutput {
	return i.ToAppOutputWithContext(context.Background())
}

func (i *App) ToAppOutputWithContext(ctx context.Context) AppOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppOutput)
}

func (i *App) ToAppPtrOutput() AppPtrOutput {
	return i.ToAppPtrOutputWithContext(context.Background())
}

func (i *App) ToAppPtrOutputWithContext(ctx context.Context) AppPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppPtrOutput)
}

type AppPtrInput interface {
	pulumi.Input

	ToAppPtrOutput() AppPtrOutput
	ToAppPtrOutputWithContext(ctx context.Context) AppPtrOutput
}

type appPtrType AppArgs

func (*appPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**App)(nil))
}

func (i *appPtrType) ToAppPtrOutput() AppPtrOutput {
	return i.ToAppPtrOutputWithContext(context.Background())
}

func (i *appPtrType) ToAppPtrOutputWithContext(ctx context.Context) AppPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppPtrOutput)
}

// AppArrayInput is an input type that accepts AppArray and AppArrayOutput values.
// You can construct a concrete instance of `AppArrayInput` via:
//
//          AppArray{ AppArgs{...} }
type AppArrayInput interface {
	pulumi.Input

	ToAppArrayOutput() AppArrayOutput
	ToAppArrayOutputWithContext(context.Context) AppArrayOutput
}

type AppArray []AppInput

func (AppArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*App)(nil))
}

func (i AppArray) ToAppArrayOutput() AppArrayOutput {
	return i.ToAppArrayOutputWithContext(context.Background())
}

func (i AppArray) ToAppArrayOutputWithContext(ctx context.Context) AppArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppArrayOutput)
}

// AppMapInput is an input type that accepts AppMap and AppMapOutput values.
// You can construct a concrete instance of `AppMapInput` via:
//
//          AppMap{ "key": AppArgs{...} }
type AppMapInput interface {
	pulumi.Input

	ToAppMapOutput() AppMapOutput
	ToAppMapOutputWithContext(context.Context) AppMapOutput
}

type AppMap map[string]AppInput

func (AppMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*App)(nil))
}

func (i AppMap) ToAppMapOutput() AppMapOutput {
	return i.ToAppMapOutputWithContext(context.Background())
}

func (i AppMap) ToAppMapOutputWithContext(ctx context.Context) AppMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppMapOutput)
}

type AppOutput struct {
	*pulumi.OutputState
}

func (AppOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*App)(nil))
}

func (o AppOutput) ToAppOutput() AppOutput {
	return o
}

func (o AppOutput) ToAppOutputWithContext(ctx context.Context) AppOutput {
	return o
}

func (o AppOutput) ToAppPtrOutput() AppPtrOutput {
	return o.ToAppPtrOutputWithContext(context.Background())
}

func (o AppOutput) ToAppPtrOutputWithContext(ctx context.Context) AppPtrOutput {
	return o.ApplyT(func(v App) *App {
		return &v
	}).(AppPtrOutput)
}

type AppPtrOutput struct {
	*pulumi.OutputState
}

func (AppPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**App)(nil))
}

func (o AppPtrOutput) ToAppPtrOutput() AppPtrOutput {
	return o
}

func (o AppPtrOutput) ToAppPtrOutputWithContext(ctx context.Context) AppPtrOutput {
	return o
}

type AppArrayOutput struct{ *pulumi.OutputState }

func (AppArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]App)(nil))
}

func (o AppArrayOutput) ToAppArrayOutput() AppArrayOutput {
	return o
}

func (o AppArrayOutput) ToAppArrayOutputWithContext(ctx context.Context) AppArrayOutput {
	return o
}

func (o AppArrayOutput) Index(i pulumi.IntInput) AppOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) App {
		return vs[0].([]App)[vs[1].(int)]
	}).(AppOutput)
}

type AppMapOutput struct{ *pulumi.OutputState }

func (AppMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]App)(nil))
}

func (o AppMapOutput) ToAppMapOutput() AppMapOutput {
	return o
}

func (o AppMapOutput) ToAppMapOutputWithContext(ctx context.Context) AppMapOutput {
	return o
}

func (o AppMapOutput) MapIndex(k pulumi.StringInput) AppOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) App {
		return vs[0].(map[string]App)[vs[1].(string)]
	}).(AppOutput)
}

func init() {
	pulumi.RegisterOutputType(AppOutput{})
	pulumi.RegisterOutputType(AppPtrOutput{})
	pulumi.RegisterOutputType(AppArrayOutput{})
	pulumi.RegisterOutputType(AppMapOutput{})
}
