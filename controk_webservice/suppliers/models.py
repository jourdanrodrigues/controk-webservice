from django.db import models

from controk_webservice.addresses.models import Address
from controk_webservice.contacts.models import Contact


class Supplier(models.Model):
    address = models.ForeignKey(Address, related_name='suppliers')
    contact = models.ForeignKey(Contact, related_name='suppliers')
    cnpj = models.CharField(max_length=20)
    trading_name = models.CharField(max_length=60)

    class Meta:
        db_table = 'Supplier'
