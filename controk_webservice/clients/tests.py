from rest_framework import status

from assets.models import CustomAPITestCase
from controk_webservice.clients.models import Client


class ClientTest(CustomAPITestCase):
    fixtures = ['clients', 'addresses']

    def test_clients_list(self):
        response = self.client.get('/api/v1/clients/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = ['id', 'name', 'email', 'cpf', 'observation']
        self.bulkAssertIn(items, response.data, is_list=True)

    def test_retrieve_client(self):
        client_id = Client.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/clients/{}/'.format(client_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = [{'address': ['place', 'place_name', 'number', 'complement', 'neighborhood', 'city', 'state', 'cep']},
                 'phone', 'mobile']
        self.bulkAssertIn(items, response.data)
