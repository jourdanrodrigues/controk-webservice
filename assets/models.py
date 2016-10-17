from django.db import models
from django.utils.translation import ugettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase

from assets.utils import is_cpf_valid


class CustomAPITestCase(APITestCase):
    request_kwargs = {'format': 'json'}

    def bulkAssertIn(self, items: list, data, is_list: bool = False):
        """
        Source: https://github.com/jourdanrodrigues/drf_test_utils/blob/master/functions.py
        :param self: object
        :param items: list of keys that must be in the "data" (list)
        :param data: dictionary (or a list of dictionaries) to be tested (dict)
        :param is_list: Applies additional tests for the list if True (bool)
        :return: Nothing
        """
        if is_list:
            self.assertIsInstance(data, list)
            if data and isinstance(data[0], dict):
                # Get the first item to check its items
                data = data[0]
            else:
                return

        # Check if these are the only attributes in the dictionary
        self.assertEqual(len(items), len(data),
                         msg='Missing attributes: ' + (', '.join([x for x in items if x not in data])
                                                       if len(items) > len(data) else
                                                       ', '.join([x for x in data if x not in items])))
        for item in items:
            # Check the existence of each field
            self.assertIn(item, data)


class Person(models.Model):
    email = models.EmailField()
    mobile = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    cpf = models.CharField(max_length=14)
    name = models.CharField(max_length=60)
    observation = models.TextField(null=True)

    def is_cpf_valid(self):
        return is_cpf_valid(self.cpf)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_cpf_valid():
            super(Person, self).save(force_insert, force_update, using, update_fields)
        else:
            raise ValidationError(_("CPF is not valid."))

    class Meta:
        abstract = True
