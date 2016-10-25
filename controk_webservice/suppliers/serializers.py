from rest_framework import serializers

from assets.models import PersonInfoSerializer
from controk_webservice.suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'email', 'cnpj', 'trading_name']


class SupplierInfoSerializer(PersonInfoSerializer):
    class Meta(PersonInfoSerializer.Meta):
        model = Supplier
