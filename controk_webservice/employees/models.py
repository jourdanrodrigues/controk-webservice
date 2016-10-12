from django.db import models

from controk_webservice.addresses.models import Address
from controk_webservice.contacts.models import Contact


class Employee(models.Model):
    address = models.ForeignKey(Address, related_name='employees')
    contact = models.ForeignKey(Contact, related_name='employees')
    role = models.CharField(max_length=40)
    cpf = models.CharField(max_length=14)
    name = models.CharField(max_length=60)
    observation = models.TextField()

    class Meta:
        db_table = 'Employee'
