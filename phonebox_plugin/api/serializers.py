from rest_framework import serializers
from core.models import ObjectType
from netbox.api.fields import ContentTypeField
from netbox.api.gfk_fields import GFKSerializerField
from netbox.api.serializers import NetBoxModelSerializer
from tenancy.api.serializers import TenantSerializer
from dcim.api.serializers import RegionSerializer, SiteSerializer
from circuits.api.serializers import ProviderSerializer
from ..models import Number, VoiceCircuit
from ..choices import VOICE_CIRCUIT_ASSIGNMENT_MODELS


class NumberSerializer(NetBoxModelSerializer):

    label = serializers.CharField(source='number', read_only=True)
    tenant = TenantSerializer(required=True, allow_null=False, nested=True)
    region = RegionSerializer(required=False, allow_null=True, nested=True)
    provider = ProviderSerializer(required=False, allow_null=True, nested=True)
    forward_to = serializers.PrimaryKeyRelatedField(queryset=Number.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Number
        fields = [
            "id", "url", "display", "label", "number", "tenant", "region", "forward_to", "description",
            "provider", "tags", "custom_fields", "created", "last_updated",
        ]
        brief_fields = ("id", "url", "display", "number", "description")


class VoiceCircuitSerializer(NetBoxModelSerializer):

    label = serializers.CharField(source='name', read_only=True)
    tenant = TenantSerializer(required=True, allow_null=False, nested=True)
    region = RegionSerializer(required=False, allow_null=True, nested=True)
    site = SiteSerializer(required=False, allow_null=True, nested=True)
    provider = ProviderSerializer(required=False, allow_null=True, nested=True)
    assigned_object_type = ContentTypeField(
        queryset=ObjectType.objects.filter(VOICE_CIRCUIT_ASSIGNMENT_MODELS),
        required=True,
        allow_null=False
    )
    assigned_object = GFKSerializerField(read_only=True)

    class Meta:
        model = VoiceCircuit
        fields = [
            "id", "url", "display", "label", "name", "voice_circuit_type", "tenant", "region", "site",
            "description", "assigned_object_type", "assigned_object_id", "assigned_object",
            "sip_source", "sip_target", "provider", "tags", "custom_fields", "created", "last_updated",
        ]
        brief_fields = ("id", "url", "display", "name", "voice_circuit_type", "description")
