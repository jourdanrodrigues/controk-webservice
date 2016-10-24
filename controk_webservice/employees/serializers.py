from rest_framework import serializers

from controk_webservice.addresses.serializers import AddressSerializer
from controk_webservice.employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    place_options = serializers.SerializerMethodField()
    address = AddressSerializer()

    @staticmethod
    def get_place_options(employee):
        return dict(employee.address.PLACES)

    class Meta:
        model = Employee
        fields = ['phone', 'mobile', 'address', 'place_options']


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'email', 'role', 'name', 'cpf', 'observation']
