from rest_framework import status

from assets.models import CustomAPITestCase
from controk_webservice.employees.models import Employee


class EmployeeTest(CustomAPITestCase):
    fixtures = ['employees.json', 'addresses.json']
    items = ['id', 'name', 'email', 'cpf', 'observation', 'role']

    def test_employees_list(self):
        response = self.client.get('/api/v1/employees/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data, is_list=True)

    def test_retrieve_employee(self):
        employee_id = Employee.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/employees/{}/'.format(employee_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data)
