from rest_framework import serializers

from controk_webservice.employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
