from rest_framework import viewsets

from assets.models import MultiSerializerViewSet
from controk_webservice.clients.serializers import Client, ClientListSerializer, ClientSerializer


class ClientsViewSet(MultiSerializerViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializers = {
        'default': ClientSerializer,
        'list': ClientListSerializer
    }
