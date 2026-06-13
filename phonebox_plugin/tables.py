import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import Number, VoiceCircuit


class NumberTable(NetBoxTable):

    number = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    region = tables.Column(linkify=True)
    provider = tables.Column(linkify=True)
    forward_to = tables.Column(linkify=True)
    tags = columns.TagColumn(url_name='plugins:phonebox_plugin:number_list')

    class Meta(NetBoxTable.Meta):
        model = Number
        fields = (
            'pk', 'id', 'number', 'tenant', 'region', 'description', 'provider', 'forward_to',
            'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = ('number', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')


class VoiceCircuitTable(NetBoxTable):

    name = tables.Column(linkify=True)
    voice_device_or_vm = tables.Column(
        accessor='assigned_object.parent_object',
        linkify=True,
        orderable=False,
        verbose_name='Device/VM'
    )
    voice_circuit_type = tables.Column()
    tenant = tables.Column(linkify=True)
    region = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    provider = tables.Column(linkify=True)
    tags = columns.TagColumn(url_name='plugins:phonebox_plugin:voicecircuit_list')

    class Meta(NetBoxTable.Meta):
        model = VoiceCircuit
        fields = (
            'pk', 'id', 'name', 'voice_device_or_vm', 'voice_circuit_type', 'tenant', 'region',
            'site', 'description', 'provider', 'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = (
            'name', 'voice_device_or_vm', 'voice_circuit_type', 'tenant', 'region', 'site', 'provider', 'tags',
        )
