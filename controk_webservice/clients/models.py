from django.db import models

from controk_webservice.addresses.models import Address


class Client(models.Model):
    address = models.ForeignKey(Address, related_name='clients')
    email = models.EmailField()
    mobile = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    cpf = models.CharField(max_length=14)
    name = models.CharField(max_length=60)
    observation = models.TextField(null=True)

    class Meta:
        db_table = 'Client'
