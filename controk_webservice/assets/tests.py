from rest_framework import status

from assets.models import CustomAPITestCase


class AssetsTest(CustomAPITestCase):
    def test_api_namespaces(self):
        response = self.client.get('/api/v1/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data_items = ['suppliers', 'employees', 'clients', 'products', 'shipments']
        self.bulkAssertIn(data_items, response.data)

    def test_place_options_list(self):
        response = self.client.get('/api/v1/assets/place_options/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data_items = ['id', 'name']
        self.bulkAssertIn(data_items, response.data, is_list=True, list_length=3)
