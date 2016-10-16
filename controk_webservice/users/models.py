from django.contrib.admin import site
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


site.register(User)
