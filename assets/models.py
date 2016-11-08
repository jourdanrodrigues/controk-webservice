from django.db import models
from rest_framework import serializers
from rest_framework.test import APITestCase

from controk_webservice.addresses.serializers import Address, AddressSerializer


def get_place_options(places: tuple=None):
    places = places or Address.PLACES
    return [{'id': key, 'name': value} for key, value in dict(places).items()]


class CustomAPITestCase(APITestCase):  # pragma: no cover
    request_kwargs = {'format': 'json'}

    def bulkAssertIn(self, items, data, is_list: bool = False, list_length: int=None):
        """
        Source: https://github.com/jourdanrodrigues/drf_test_utils/blob/master/functions.py
        :param self: object
        :param items: list of keys that must be in the "data" (list)
        :param data: dictionary (or a list of dictionaries) to be tested (dict)
        :param is_list: Applies additional tests for the list if True (bool)
        :param list_length: Length of the list sent (ignored if "is_list" is false)
        :return: Nothing
        """
        if is_list:
            self.assertIsInstance(data, list)
            if list_length is not None:
                self.assertEqual(len(data), list_length)
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
                                raise AssertionError('"{}" missing "entries" or "value" key.'.format(key))

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

    class Meta:
        abstract = True


class PersonInfoSerializer(serializers.ModelSerializer):
    place_options = serializers.SerializerMethodField()
    address = AddressSerializer()

    @staticmethod
    def get_place_options(person):
        return get_place_options(person.address.PLACES)

    class Meta:
        fields = ['phone', 'mobile', 'address', 'place_options']
