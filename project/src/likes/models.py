# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', verbose_name=u'Автор')
    created = models.DateTimeField(auto_now=True, verbose_name=u'Время лайка')
    question = models.ForeignKey('questions.Question', blank=True, null=True,
                                 related_name='likes', verbose_name=u'Понравившийся вопрос')
    comment = models.ForeignKey('comments.Comment', blank=True, null=True,
                                related_name='likes', verbose_name=u'Понравившийся комментарий')
    is_archive = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'
        ordering = 'id', 'author'

    def __unicode__(self):
        if self.question is not None:
            return u'Лайк от {} вопросу {}'.format(self.author.username, self.question)
        if self.comment is not None:
            return u'Лайк от {} комментарию {}'.format(self.author.username, self.comment)
