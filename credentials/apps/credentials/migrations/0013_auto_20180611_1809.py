# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-11 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0012_programcertificate_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programcertificate',
            name='language',
            field=models.CharField(help_text='Locale in which certificates for this program will be rendered', max_length=8, null=True),
        ),
    ]
