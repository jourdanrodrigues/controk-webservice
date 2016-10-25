from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from controk_webservice.clients.serializers import Client, ClientSerializer, ClientInfoSerializer


class ClientsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @detail_route(methods=['GET'])
    def info(self, request, pk):
        employee = get_object_or_404(self.queryset.select_related('address'), pk=pk)

        return Response(ClientInfoSerializer(employee).data)
