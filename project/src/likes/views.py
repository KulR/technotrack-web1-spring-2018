# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.forms import forms
from .models import Like
from questions.models import Question
from comments.models import Comment


def CreateLikeQuestion(request, pk):
    # CreateLike(request, pk, Question)
    return HttpResponse(CreateLike(request, pk, Question))
    # return redirect('questions:questions_detail', pk=pk)


def CreateLikeComment(request, pk):
    return HttpResponse(CreateLike(request, pk, Comment))
    # comment = get_object_or_404(Comment, id=pk)
    # return redirect('questions:questions_detail', pk=comment.question_id)


def CreateLike(request, pk, model):
    liked_object = get_object_or_404(model, id=pk)
    try:
        like = liked_object.likes.get(author=request.user)
        like.is_archive = not like.is_archive
        like.save()
    except:
        like1 = Like(liked_object=liked_object, author=request.user)
        like1.save()
    return liked_object.likes.filter(is_archive=False).count()

