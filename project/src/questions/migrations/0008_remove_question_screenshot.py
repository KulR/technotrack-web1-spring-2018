# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-23 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_question_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='screenshot',
        ),
    ]