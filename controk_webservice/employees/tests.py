from django.utils.translation import gettext as _
from rest_framework import status

from assets.models import CustomAPITestCase
from controk_webservice.employees.models import Address, Employee


class EmployeeTest(CustomAPITestCase):
    fixtures = ['employees', 'addresses']

    def test_employees_list(self):
        response = self.client.get('/api/v1/employees/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = ['id', 'name', 'email', 'cpf', 'observation', 'role']
        self.bulkAssertIn(items, response.data, is_list=True)

    def test_retrieve_employee(self):
        employee_id = Employee.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/employees/{}/'.format(employee_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = ['id', 'name', 'email', 'cpf', 'observation', 'role']
        self.bulkAssertIn(items, response.data)

    def test_retrieve_nonexistent_employee(self):
        response = self.client.get('/api/v1/employees/0/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.bulkAssertIn(['detail'], response.data)
        self.assertEqual(response.data['detail'], _('Not found.'))

    def test_retrieve_employee_info(self):
        employee_id = Employee.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/employees/{}/info/'.format(employee_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = [{'address': ['place', 'place_name', 'number', 'complement', 'neighborhood', 'city', 'state', 'cep'],
                  'place_options': dict(Address.PLACES).keys()},
                 'phone', 'mobile']
        self.bulkAssertIn(items, response.data)

    def test_retrieve_nonexistent_employee_info(self):
        response = self.client.get('/api/v1/employees/0/info/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.bulkAssertIn(['detail'], response.data)
        self.assertEqual(response.data['detail'], _('Not found.'))
