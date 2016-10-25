from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from controk_webservice.suppliers.serializers import Supplier, SupplierInfoSerializer, SupplierSerializer


class SuppliersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @detail_route(methods=['GET'])
    def info(self, request, pk):
        employee = get_object_or_404(self.queryset.select_related('address'), pk=pk)

        return Response(SupplierInfoSerializer(employee).data)
