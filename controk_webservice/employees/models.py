from django.contrib.admin import site
from django.db import models

from controk_webservice.addresses.models import Address


class Employee(models.Model):
    address = models.ForeignKey(Address, related_name='employees')
    email = models.EmailField()
    mobile = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    cpf = models.CharField(max_length=14)
    name = models.CharField(max_length=60)
    observation = models.TextField(null=True)
    role = models.CharField(max_length=40)

    class Meta:
        db_table = 'Employee'


site.register(Employee)
