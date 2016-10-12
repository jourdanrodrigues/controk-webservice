from django.db import models


class Address(models.Model):
    STREET = 1
    AVENUE = 2
    SIDE_STREET = 3
    PLACES = (
        (STREET, 'Rua'),
        (AVENUE, 'Avenida'),
        (SIDE_STREET, 'Travessa'),
    )

    place = models.CharField(choices=PLACES, max_length=20)
    place_name = models.CharField(max_length=60)
    number = models.IntegerField(null=True)
    complement = models.CharField(max_length=20, null=True)
    neighborhood = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)

    class Meta:
        db_table = 'Address'
