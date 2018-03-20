# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question

def question_list(request):
    context = {
        'questions': Question.objects.all(),
    }
    return render(request, 'questions/questions_list.html', context)


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    comments = question.comments.all().filter(comment=None, is_archive=False)
    context = {
        'question': question,
        'comments': comments,
    }
    return render(request, 'questions/question_detail.html', context)

def change_question(request, pk):
    return HttpResponse("You change the {} category page".format(pk))
