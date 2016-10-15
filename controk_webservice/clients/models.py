from django.db import models

from controk_webservice.addresses.models import Address
from controk_webservice.contacts.models import Contact


class Client(models.Model):
    address = models.ForeignKey(Address, related_name='clients')
    contact = models.ForeignKey(Contact, related_name='clients')
    cpf = models.CharField(max_length=14)
    name = models.CharField(max_length=60)
    observation = models.TextField(null=True)

    class Meta:
        db_table = 'Client'
