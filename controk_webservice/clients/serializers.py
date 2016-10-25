from rest_framework import serializers

from assets.models import PersonInfoSerializer
from controk_webservice.clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'cpf', 'observation']


class ClientInfoSerializer(PersonInfoSerializer):
    class Meta(PersonInfoSerializer.Meta):
        model = Client
