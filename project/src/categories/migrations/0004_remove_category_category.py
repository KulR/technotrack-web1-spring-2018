# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20180318_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
    ]
