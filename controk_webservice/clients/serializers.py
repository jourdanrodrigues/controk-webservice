from rest_framework import serializers

from controk_webservice.addresses.serializers import AddressSerializer
from controk_webservice.clients.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'cpf', 'observation']


class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Client
        fields = ['phone', 'mobile', 'address']
