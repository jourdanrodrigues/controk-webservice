from django.db import models

from controk_webservice.addresses.models import Address


class Supplier(models.Model):
    address = models.ForeignKey(Address, related_name='suppliers')
    email = models.EmailField()
    mobile = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    cnpj = models.CharField(max_length=20)
    trading_name = models.CharField(max_length=60)

    class Meta:
        db_table = 'Supplier'
