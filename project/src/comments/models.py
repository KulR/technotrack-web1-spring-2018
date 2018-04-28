# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from likes.models import Like
from django.contrib.contenttypes.fields import GenericRelation


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', verbose_name=u'Автор')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    question = models.ForeignKey('questions.Question', related_name='comments', verbose_name=u'Вопрос')
    comment = models.ForeignKey('self', blank=True, null=True, related_name='comments',
                                verbose_name=u'Родительский комментарий')
    text = models.TextField(verbose_name=u'Содержание комментария')
    likes = GenericRelation(Like, null=True, blank=True)
    is_archive = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = 'id', "question"

    def __unicode__(self):
        created = self.created
        result = "{} {:02d}.{:02d}.{} в {:02d}:{:02d}".format(self.author.username, created.day, created.month,
                                              created.year, created.hour, created.minute)
        return result

    def print_comment(self, indent=0):
        result = ""
        if self.comments.all().count() == 0:
            return "{}{}\n{}{}\n{}{}{}\n\n".format("\t"*indent, self, "\t"*indent, self.text,
                                                   "\t"*indent, self.like.count(), "Likes")
        else:
            result += "{}{}\n{}{}\n{}{}{}\n".format("\t"*indent, self, "\t"*indent, self.text,
                                                    "\t"*indent, self.like.count(), "Likes")
            for comment in self.comments.all():
                if not comment.is_archive:
                    result += "{}".format(comment.print_comment(indent+1))
            return result
