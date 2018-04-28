# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from likes.models import Like
from django.contrib.contenttypes.fields import GenericRelation
import os



class Question(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название вопроса')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', verbose_name=u'Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Время создания')
    updated = models.DateTimeField(auto_now=True,  verbose_name=u'Время редактирования')
    categories = models.ManyToManyField('categories.Category', related_name='questions', verbose_name=u'Категории')
    text = models.TextField(verbose_name=u'Вопрос')
    likes = GenericRelation(Like, null=True, blank=True)
    is_archive = models.BooleanField(default=False, verbose_name=u'В архиве')

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = 'name', 'created'


    def __unicode__(self):
        return self.name
