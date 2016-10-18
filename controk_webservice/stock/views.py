from rest_framework import viewsets

from controk_webservice.stock.serializers import (Product, Shipment,
                                                  ProductSerializer, ShipmentSerializer)


class ShipmentsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
