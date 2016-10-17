from django.contrib.admin import site
from django.db import models

from assets.models import Person
from controk_webservice.addresses.models import Address


class Client(Person):
    address = models.ForeignKey(Address, related_name='clients')

    class Meta:
        db_table = 'Client'


site.register(Client)
