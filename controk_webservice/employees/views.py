from rest_framework import viewsets

from assets.models import MultiSerializerViewSet
from controk_webservice.employees.serializers import Employee, EmployeeSerializer, EmployeeListSerializer


class EmployeesViewSet(MultiSerializerViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializers = {
        'default': EmployeeSerializer,
        'list': EmployeeListSerializer
    }

    def get_queryset(self):
        queryset = self.queryset

        # Bring the address within the main query only on retrieve
        if self.action == 'retrieve':
            queryset = queryset.select_related('address')

        return queryset
