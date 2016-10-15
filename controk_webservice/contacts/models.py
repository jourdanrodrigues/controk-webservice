from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'Contact'
