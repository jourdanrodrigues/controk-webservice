from rest_framework import viewsets

from controk_webservice.employees.serializers import Employee, EmployeeSerializer


class EmployeesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
