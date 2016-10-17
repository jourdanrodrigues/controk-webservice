from rest_framework import status

from assets.models import CustomAPITestCase


class EmployeeTest(CustomAPITestCase):
    def test_employees_list(self):
        response = self.client.get('/api/v1/employees/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data_items = ['id', 'name', 'email', 'cpf', 'observation', 'role']
        self.bulkAssertIn(data_items, response.data, is_list=True)
