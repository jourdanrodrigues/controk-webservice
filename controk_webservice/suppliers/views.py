from rest_framework import viewsets

from assets.models import MultiSerializerViewSet
from controk_webservice.suppliers.serializers import Supplier, SupplierSerializer, SupplierListSerializer


class SuppliersViewSet(MultiSerializerViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.objects.all()
    serializers = {
        'default': SupplierSerializer,
        'list': SupplierListSerializer
    }

    def get_queryset(self):
        queryset = self.queryset

        # Bring the address within the main query only on retrieve
        if self.action == 'retrieve':
            queryset = queryset.select_related('address')

        return queryset
