# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):

    list_display = 'id', '__unicode__', 'question', 'author', 'comment'
    search_fields = 'question__name', 'author__username', '__unicode__'
    list_filter = 'is_archive', 'author__username'
