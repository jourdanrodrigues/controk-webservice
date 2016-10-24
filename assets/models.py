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

    def bulkAssertIn(self, items, data, is_list: bool = False):
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

        def which_params(missing, containing):
            def mount_list(attributes, its_list):
                for attribute in attributes:
                    if isinstance(attribute, dict):
                        its_list += list(attribute.keys())
                    else:
                        its_list.append(attribute)

            missing_attributes = []
            containing_attributes = []

            mount_list(missing, missing_attributes)
            mount_list(containing, containing_attributes)

            return ', '.join([x for x in missing_attributes if x not in containing_attributes])

        def bulk_test(entries: list, target: dict):
            len_entries = 0

            # Check each entry
            for entry in entries:
                # If entry is a dict, target has sub items
                if isinstance(entry, dict):
                    for key, sub_entries in entry.items():
                        len_entries += 1

                        if isinstance(sub_entries, dict):  # Has a configuration
                            if sub_entries.get('is_list'):
                                target[key] = target[key][0]
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
                    len_entries += 1
                    self.assertIn(entry, target)

            # Check if these are the only attributes in the dictionary
            self.assertEqual(len_entries, len(target),
                             msg='Missing keys: {}.'.format(which_params(entries, target)
                                                            if len_entries > len(target) else
                                                            which_params(target, entries)))

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
