from rest_framework import status

from assets.models import CustomAPITestCase


class ClientTest(CustomAPITestCase):
    def test_clients_list(self):
        response = self.client.get('/api/v1/clients/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data_items = ['id', 'name', 'email', 'cpf', 'observation']
        self.bulkAssertIn(data_items, response.data, is_list=True)
