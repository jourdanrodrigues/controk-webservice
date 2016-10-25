from rest_framework import serializers

from controk_webservice.addresses.serializers import AddressSerializer
from controk_webservice.clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'cpf', 'observation']


class ClientInfoSerializer(serializers.ModelSerializer):
    place_options = serializers.SerializerMethodField()
    address = AddressSerializer()

    @staticmethod
    def get_place_options(client):
        return dict(client.address.PLACES)

    class Meta:
        model = Client
        fields = ['phone', 'mobile', 'address', 'place_options']
