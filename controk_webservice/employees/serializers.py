from rest_framework import serializers

from assets.models import PersonInfoSerializer
from controk_webservice.employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'email', 'role', 'name', 'cpf', 'observation']


class EmployeeInfoSerializer(PersonInfoSerializer):
    class Meta(PersonInfoSerializer.Meta):
        model = Employee
