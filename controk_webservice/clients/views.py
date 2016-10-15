from rest_framework import viewsets

from controk_webservice.clients.serializers import Client, ClientSerializer


class ClientsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
