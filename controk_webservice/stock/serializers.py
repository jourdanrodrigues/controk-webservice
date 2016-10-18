from rest_framework import serializers

from controk_webservice.stock.models import Product, Shipment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'description', 'cost', 'name', 'sell_value']


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id', 'delivery_date', 'payment_date', 'order_date']
