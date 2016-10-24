from rest_framework import viewsets

from assets.models import MultiSerializerViewSet
from controk_webservice.clients.serializers import Client, ClientListSerializer, ClientSerializer


class ClientsViewSet(MultiSerializerViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializers = {
        'default': ClientSerializer,
        'list': ClientListSerializer
    }

    def get_queryset(self):
        queryset = self.queryset

        # Bring the address within the main query only on retrieve
        if self.action == 'retrieve':
            queryset = queryset.select_related('address')

        return queryset
