# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 18:05
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180423_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.pathToAvatars, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440'),
        ),
    ]
