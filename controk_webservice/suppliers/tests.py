from rest_framework import status

from assets.models import CustomAPITestCase
from controk_webservice.suppliers.models import Supplier


class EmployeeTest(CustomAPITestCase):
    fixtures = ['suppliers.json', 'addresses.json']
    items = ['id', 'email', 'cnpj', 'trading_name']

    def test_suppliers_list(self):
        response = self.client.get('/api/v1/suppliers/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data, is_list=True)

    def test_retrieve_supplier(self):
        supplier_id = Supplier.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/suppliers/{}/'.format(supplier_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data)
