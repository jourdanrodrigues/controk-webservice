from rest_framework import serializers

from controk_webservice.addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['place', 'place_name', 'number', 'complement', 'neighborhood', 'city', 'state', 'cep']
