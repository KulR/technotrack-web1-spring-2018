# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name=u'Название категории')
#   author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='categories', verbose_name=u'Автор')
#    questions = models.ManyToManyField('questions.Question', related_name='questions', verbose_name=u'Вопросы')
    is_archive = models.BooleanField(default=False, verbose_name=u'В архиве')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Время создания')
    updated = models.DateTimeField(auto_now=True,  verbose_name=u'Время редактирования')

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = "name", 'created'

    def __unicode__(self):
        return self.name
