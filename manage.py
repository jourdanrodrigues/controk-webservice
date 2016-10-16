#!/usr/bin/env python
import os
import sys

from re import match


def read_env():
    """
    https://gist.github.com/bennylope/2999704
    """
    try:
        with open('.env') as f:
            content = f.read()
    except IOError:
        content = ''

    for line in content.splitlines():
        m1 = match(r'\A(?P<key>[A-Za-z_0-9]+)=(?P<value>.*)\Z', line)
        if m1:
            os.environ.setdefault(**m1.groupdict())

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controk_webservice.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    read_env()
    execute_from_command_line(sys.argv)
