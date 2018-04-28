# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.shortcuts import render, get_object_or_404, reverse, redirect

from .models import Question
from django.views.generic import CreateView, UpdateView
from .form import QuestionListForm


class NewQuestion(CreateView):
    model = Question
    fields = 'name', 'categories', 'text'
    context_object_name = 'question'
    template_name = 'questions/new_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewQuestion, self).form_valid(form)

    def get_success_url(self):
        return reverse('questions:questions_detail', kwargs={'pk': self.object.pk})


class ChangeQuestion(UpdateView):
    model = Question
    fields = 'name', 'categories', 'text'
    context_object_name = 'question'
    template_name = 'questions/update_question.html'

    def get_success_url(self):
        return reverse('questions:questions_detail', kwargs={'pk': self.object.pk})


def question_list(request):
    questions = Question.objects.all()
    form = QuestionListForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['sort']:
            questions = questions.order_by(form.cleaned_data['sort'])
        if form.cleaned_data['search']:
            questions = questions.filter(name__icontains=form.cleaned_data['search'])
    context = {
        'questions': questions,
        'form': form,
    }
    return render(request, 'questions/questions_list.html', context)


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    comments = question.comments.filter(is_archive=False).order_by("created")
    question_likes = question.likes.filter(is_archive=False)

    comment_list = []
    for comment in comments:
        comment.likes_qs = comment.likes.filter(is_archive=False)
        comment.liked = 0
        if request.user.id is not None:
            comment.liked = comment.likes.filter(is_archive=False, author=request.user).count()
        comment_list.append(comment)
    question.likes_qs = question.likes.filter(is_archive=False)
    question.liked = 0
    if request.user.id is not None:
        question.liked = question.likes.filter(is_archive=False, author=request.user).count()

    context = {
        'question': question,
        'comments': comment_list,
        'question_likes': question_likes,
    }
    return render(request, 'questions/question_detail.html', context)


def delete_question(request, pk):
    question = get_object_or_404(Question, id=pk)
    if question.author == request.user or request.user.is_staff:
        question.is_archive = True
        question.save()
    return redirect('core:lk')
