from django import forms
from tenancy.models import Tenant
from dcim.models import Region, Site, Device, Interface
from virtualization.models import VirtualMachine, VMInterface
from circuits.models import Provider
from netbox.forms import (
    NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm,
)
from utilities.forms.fields import (
    DynamicModelChoiceField, DynamicModelMultipleChoiceField, TagFilterField, CSVModelChoiceField,
)
from .models import Number, VoiceCircuit
from .choices import VoiceCircuitTypeChoices


class NumberFilterForm(NetBoxModelFilterSetForm):

    model = Number
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    region = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        required=False,
    )
    provider = DynamicModelMultipleChoiceField(
        queryset=Provider.objects.all(),
        required=False,
    )
    tag = TagFilterField(model)


class NumberEditForm(NetBoxModelForm):

    number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'off',
                'pattern': r'^\+?[0-9A-D\*\#]+$',
                'title': 'Enter the Phone Number'
            }
        )
    )

    class Meta:
        model = Number
        fields = ('number', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')


class NumberBulkEditForm(NetBoxModelBulkEditForm):

    model = Number

    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
    )
    provider = DynamicModelChoiceField(
        queryset=Provider.objects.all(),
        required=False,
    )
    forward_to = DynamicModelChoiceField(
        queryset=Number.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    nullable_fields = ('region', 'provider', 'forward_to', 'description')


class NumberImportForm(NetBoxModelImportForm):
    tenant = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Assigned tenant'
    )
    provider = CSVModelChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='name',
        required=False,
        help_text='Originating provider'
    )
    region = CSVModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Assigned region'
    )
    forward_to = CSVModelChoiceField(
        queryset=Number.objects.all(),
        to_field_name="number",
        required=False,
        help_text='Optional call forwarding Number'
    )

    class Meta:
        model = Number
        fields = ('number', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')


class VoiceCircuitEditForm(NetBoxModelForm):

    name = forms.CharField(
        required=True,
    )
    voice_circuit_type = forms.ChoiceField(
        choices=VoiceCircuitTypeChoices
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        initial_params={
            'interfaces': '$interface'
        }
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        required=False,
        query_params={
            'device_id': '$device'
        }
    )
    virtual_machine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        initial_params={
            'interfaces': '$vminterface'
        }
    )
    vminterface = DynamicModelChoiceField(
        queryset=VMInterface.objects.all(),
        required=False,
        label='Interface',
        query_params={
            'virtual_machine_id': '$virtual_machine'
        }
    )

    class Meta:
        model = VoiceCircuit
        fields = (
            'name', 'voice_circuit_type', 'tenant', 'region', 'site',
            'description', 'provider', 'provider_circuit_id', 'tags',
            'sip_source', 'sip_target'
        )

    def __init__(self, *args, **kwargs):

        # Initialize helper selectors
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {}).copy()
        if instance:
            if type(instance.assigned_object) is Interface:
                initial['interface'] = instance.assigned_object
            elif type(instance.assigned_object) is VMInterface:
                initial['vminterface'] = instance.assigned_object

        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

        # Cannot select both a device interface and a VM interface
        if self.cleaned_data.get('interface') and self.cleaned_data.get('vminterface'):
            raise forms.ValidationError("Cannot select both a device interface and a virtual machine interface")
        if not (self.cleaned_data.get('interface') or self.cleaned_data.get('vminterface')):
            raise forms.ValidationError("Voice Circuit must be attached to a device interface or a VM interface")
        self.instance.assigned_object = self.cleaned_data.get('interface') or self.cleaned_data.get('vminterface')


class VoiceCircuitFilterForm(NetBoxModelFilterSetForm):

    model = VoiceCircuit
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    region = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        required=False,
    )
    site = DynamicModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )
    provider = DynamicModelMultipleChoiceField(
        queryset=Provider.objects.all(),
        required=False,
    )
    tag = TagFilterField(model)


class VoiceCircuitBulkEditForm(NetBoxModelBulkEditForm):

    model = VoiceCircuit

    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
    )
    provider = DynamicModelChoiceField(
        queryset=Provider.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    nullable_fields = ('region', 'provider', 'description')


class VoiceCircuitImportForm(NetBoxModelImportForm):

    tenant = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Assigned tenant'
    )
    provider = CSVModelChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='name',
        required=False,
        help_text='Originating provider'
    )
    site = CSVModelChoiceField(
        queryset=Site.objects.all(),
        to_field_name='name',
        required=False,
        help_text='Assigned site'
    )
    region = CSVModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Assigned region'
    )

    class Meta:
        model = VoiceCircuit
        fields = (
            'name', 'voice_circuit_type', 'tenant', 'region', 'site',
            'description', 'provider', 'provider_circuit_id', 'tags',
        )
