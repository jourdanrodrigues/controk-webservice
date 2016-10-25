from django.utils.translation import gettext as _
from rest_framework import status

from assets.models import CustomAPITestCase
from controk_webservice.suppliers.models import Supplier


class EmployeeTest(CustomAPITestCase):
    fixtures = ['suppliers', 'addresses']

    def test_suppliers_list(self):
        response = self.client.get('/api/v1/suppliers/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = ['id', 'email', 'cnpj', 'trading_name']
        self.bulkAssertIn(items, response.data, is_list=True)

    def test_retrieve_supplier(self):
        supplier_id = Supplier.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/suppliers/{}/'.format(supplier_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = ['id', 'email', 'cnpj', 'trading_name']
        self.bulkAssertIn(items, response.data)

    def test_retrieve_nonexistent_supplier(self):
        response = self.client.get('/api/v1/suppliers/0/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.bulkAssertIn(['detail'], response.data)
        self.assertEqual(response.data['detail'], _('Not found.'))

    def test_retrieve_supplier_info(self):
        supplier_id = Supplier.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/suppliers/{}/info/'.format(supplier_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = [{'address': ['place', 'place_name', 'number', 'complement', 'neighborhood', 'city', 'state', 'cep'],
                  'place_options': {'is_list': True, 'entries': ['id', 'name']}},
                 'phone', 'mobile']
        self.bulkAssertIn(items, response.data)

    def test_retrieve_nonexistent_supplier_info(self):
        response = self.client.get('/api/v1/suppliers/0/info/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.bulkAssertIn(['detail'], response.data)
        self.assertEqual(response.data['detail'], _('Not found.'))
