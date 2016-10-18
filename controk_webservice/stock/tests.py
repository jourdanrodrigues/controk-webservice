from rest_framework import status

from assets.models import CustomAPITestCase
from controk_webservice.stock.models import Product, Shipment


class ProductTest(CustomAPITestCase):
    fixtures = ['products']
    items = ['id', 'description', 'cost', 'name', 'sell_value']

    def test_products_list(self):
        response = self.client.get('/api/v1/products/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data, is_list=True)

    def test_retrieve_product(self):
        product_id = Product.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/products/{}/'.format(product_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data)


class ShipmentTest(CustomAPITestCase):
    fixtures = ['shipments', 'suppliers', 'addresses']
    items = ['id', 'delivery_date', 'payment_date', 'order_date']

    def test_shipments_list(self):
        response = self.client.get('/api/v1/shipments/', **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data, is_list=True)

    def test_retrieve_shipment(self):
        shipment_id = Shipment.objects.values_list('id', flat=True).first()
        response = self.client.get('/api/v1/shipments/{}/'.format(shipment_id), **self.request_kwargs)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bulkAssertIn(self.items, response.data)
