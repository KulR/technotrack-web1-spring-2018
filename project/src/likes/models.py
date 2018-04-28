# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', verbose_name=u'Автор')
    created = models.DateTimeField(auto_now=True, verbose_name=u'Время лайка')
    # question = models.ForeignKey('questions.Question', blank=True, null=True,
    #                              related_name='likes', verbose_name=u'Понравившийся вопрос')
    # comment = models.ForeignKey('comments.Comment', blank=True, null=True,
    #                             related_name='likes', verbose_name=u'Понравившийся комментарий')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    liked_object = GenericForeignKey('content_type', 'object_id')
    is_archive = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'
        ordering = 'id', 'author'

    def __unicode__(self):
        return u'Лайк от {} к {} {}'.format(self.author.username, self.content_type, self.liked_object)
        # if self.question is not None:
        #     return u'Лайк от {} вопросу {}'.format(self.author.username, self.question)
        # if self.comment is not None:
        #     return u'Лайк от {} комментарию {}'.format(self.author.username, self.comment)
