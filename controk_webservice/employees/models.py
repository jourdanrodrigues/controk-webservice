from django.contrib.admin import site
from django.db import models

from assets.models import Person
from controk_webservice.addresses.models import Address


class Employee(Person):
    address = models.ForeignKey(Address, related_name='employees')
    role = models.CharField(max_length=40)

    class Meta:
        db_table = 'Employee'


site.register(Employee)
