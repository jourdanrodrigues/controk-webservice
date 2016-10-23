from django.db import models
from django.utils.translation import ugettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework.viewsets import GenericViewSet

from assets.utils import is_cpf_valid


class MultiSerializerViewSet(GenericViewSet):
    serializers = {'default': None}

    def get_serializer_class(self):
        assert self.serializers.get('default') is not None, (
            "'%s' should include a `serializers` attribute as a dictionary"
            " with a `default` key containing the serializer."
            % self.__class__.__name__
        )

        return self.serializers.get(self.action, self.serializers.get('default'))


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

        def bulk_test(entries, target: dict):
            # Check if these are the only attributes in the dictionary
            self.assertEqual(len(entries), len(target),
                             msg='Missing keys: {}.'.format(', '.join([x for x in entries if x not in target])
                                                            if len(entries) > len(target) else
                                                            ', '.join([x for x in target if x not in entries])))
            # Check each entry
            for entry in entries:
                # If entry is a dict, target has sub items
                if isinstance(entry, dict):
                    for key, sub_entries in entry.items():
                        if isinstance(sub_entries, dict):  # Has a configuration
                            if sub_entries.get('is_list'):
                                target = target[0]
                            if sub_entries.get('entries'):
                                sub_entries = sub_entries.get('entries')  # List of entries to test
                            elif sub_entries.get('value'):
                                self.assertEqual(sub_entries['value'], target[key],  # Test specific value
                                                 msg='"{key}": "{0} != {1}"'.format(sub_entries['value'], target[key],
                                                                                    key=key))
                                continue
                            else:
                                raise AssertionError('"{}" missing "entries" or "key" key.'.format(key))

                        self.assertIn(key, target, msg='"{}" key missing.')
                        bulk_test(sub_entries, target[key])
                else:
                    self.assertIn(entry, target)

        bulk_test(items, data)


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
