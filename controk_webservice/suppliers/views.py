from rest_framework import viewsets

from controk_webservice.suppliers.serializers import Supplier, SupplierSerializer


class SuppliersViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
