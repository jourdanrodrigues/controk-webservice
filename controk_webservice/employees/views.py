from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from controk_webservice.employees.serializers import Employee, EmployeeInfoSerializer, EmployeeSerializer


class EmployeesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @detail_route(methods=['GET'])
    def info(self, request, pk):
        employee = get_object_or_404(self.queryset.select_related('address'), pk=pk)

        return Response(EmployeeInfoSerializer(employee).data)
