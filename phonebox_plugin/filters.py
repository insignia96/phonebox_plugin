import django_filters
from django.db.models import Q
from circuits.models import Provider
from dcim.models import Region, Site
from tenancy.models import Tenant
from netbox.filtersets import NetBoxModelFilterSet
from .models import Number, VoiceCircuit


class NumberFilterSet(NetBoxModelFilterSet):

    number = django_filters.ModelMultipleChoiceFilter(
        field_name='number',
        queryset=Number.objects.all(),
        to_field_name='number',
        label='Number',
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name='tenant__id',
        to_field_name='id',
        label='Tenant (id)',
    )
    region = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='region__id',
        to_field_name='id',
        label='Region (id)',
    )
    provider = django_filters.ModelMultipleChoiceFilter(
        queryset=Provider.objects.all(),
        field_name='provider__id',
        to_field_name='id',
        label='Provider (id)',
    )
    forward_to = django_filters.ModelMultipleChoiceFilter(
        field_name='forward_to',
        queryset=Number.objects.all(),
        to_field_name='number',
        label='Forward to',
    )

    class Meta:
        model = Number
        fields = ('id', 'number', 'description')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(number__icontains=value) |
            Q(description__icontains=value)
        )


class VoiceCircuitFilterSet(NetBoxModelFilterSet):

    name = django_filters.ModelMultipleChoiceFilter(
        field_name='name',
        queryset=VoiceCircuit.objects.all(),
        to_field_name='name',
        label='Name',
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name='tenant__id',
        to_field_name='id',
        label='Tenant (id)',
    )
    site = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        field_name='site__id',
        to_field_name='id',
        label='Site (id)',
    )
    region = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='region__id',
        to_field_name='id',
        label='Region (id)',
    )
    provider = django_filters.ModelMultipleChoiceFilter(
        queryset=Provider.objects.all(),
        field_name='provider__id',
        to_field_name='id',
        label='Provider (id)',
    )

    class Meta:
        model = VoiceCircuit
        fields = ('id', 'name', 'voice_circuit_type', 'description')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )
