# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=60)),
                ('observation', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='addresses.Address')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='contacts.Contact')),
            ],
            options={
                'db_table': 'Client',
            },
        ),
    ]
