# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-23 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='data',
            field=models.DateTimeField(null=True),
        ),
    ]