# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-26 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='data',
        ),
    ]
