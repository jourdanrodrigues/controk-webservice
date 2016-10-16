from datetime import datetime

from django.contrib.admin import site
from django.db import models

from controk_webservice.employees.models import Employee
from controk_webservice.suppliers.models import Supplier


class Shipment(models.Model):
    supplier = models.ForeignKey(Supplier, related_name='shipments')
    delivery_date = models.DateField()
    payment_date = models.DateField()
    order_date = models.DateField()

    class Meta:
        db_table = 'Shipment'


class Product(models.Model):
    description = models.TextField()
    cost = models.FloatField()
    name = models.CharField(max_length=60)
    sell_value = models.FloatField()

    class Meta:
        db_table = 'Product'


class ProductShipment(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='products')
    product = models.ForeignKey(Product, related_name='shipments')
    quantity = models.IntegerField()

    class Meta:
        db_table = 'ProductShipment'


class Stock(models.Model):
    product = models.OneToOneField(Product, primary_key=True, related_name='stock')
    quantity = models.IntegerField()

    class Meta:
        db_table = 'Stock'


class StockHistory(models.Model):
    stock_product = models.ForeignKey(Stock, related_name='history')
    employee = models.ForeignKey(Employee, related_name='stock_history')
    date_time = models.DateTimeField(editable=False, default=datetime.now)
    quantity_withdraw = models.IntegerField()

    class Meta:
        db_table = 'StockHistory'


site.register(Shipment)
site.register(Stock)
site.register(StockHistory)
site.register(ProductShipment)
site.register(Product)
