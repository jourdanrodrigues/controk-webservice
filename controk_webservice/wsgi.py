import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controk_webservice.settings")

application = get_wsgi_application()
