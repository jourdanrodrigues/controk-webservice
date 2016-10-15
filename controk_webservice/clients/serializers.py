from rest_framework import serializers

from controk_webservice.clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
