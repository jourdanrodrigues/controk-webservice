from rest_framework import serializers

from controk_webservice.addresses.serializers import AddressSerializer
from controk_webservice.suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    place_options = serializers.SerializerMethodField()
    address = AddressSerializer()

    @staticmethod
    def get_place_options(supplier):
        return dict(supplier.address.PLACES)

    class Meta:
        model = Supplier
        fields = ['phone', 'mobile', 'address', 'place_options']


class SupplierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'email', 'cnpj', 'trading_name']
