from rest_framework.routers import APIRootView
from netbox.api.viewsets import NetBoxModelViewSet
from .. import filters
from ..models import Number, VoiceCircuit
from . import serializers


class PhoneBoxPluginRootView(APIRootView):
    """
    phonebox_plugin API root view
    """
    def get_view_name(self):
        return 'PhoneBox'


class NumberViewSet(NetBoxModelViewSet):
    queryset = Number.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.NumberSerializer
    filterset_class = filters.NumberFilterSet


class VoiceCircuitsViewSet(NetBoxModelViewSet):
    queryset = VoiceCircuit.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.VoiceCircuitSerializer
    filterset_class = filters.VoiceCircuitFilterSet
