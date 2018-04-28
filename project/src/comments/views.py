# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import forms
from django.db import models
from django.shortcuts import reverse, get_object_or_404, redirect
from .models import Comment
from django.views.generic import CreateView, UpdateView
from forms import MyCreateView

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'text',


# class NewComment(MyCreateView):
#     model = Comment
#     fields = 'text',
#     context_object_name = 'Comment'
#     template_name = 'comments/new_comment.html'
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         # data = form.cleaned_data
#         # form.instance.question__id = self.request.q_id
#         # if self.request.com_id != 0:
#         #     form.instance.comment__id = self.request.com_id
#         # else:
#         #     form.instance.comment__id = None
#         # form.instance.question_id = self.request.GET.get('q_id')
#         # if self.request.GET.get('com_id') is not None:
#         #     form.instance.comment_id = self.request.GET.get('com_id')
#         # else:
#         #     form.instance.comment = None
#
#         # form.instance.question__id = int(data['question_id'])
#         # if self.request.GET.get('prev_comment_id') is None:
#         #     form.instance.comment__id = None
#         # else:
#         #     form.instance.comment__id = int(self.request.GET.get('prev_comment_id'))
#         return super(NewComment, self).form_valid(form)
#
#
# def get_success_url(self):
#     return reverse('questions:questions_detail', kwargs={'pk': self.question.id})


# def change_comment(request, pk):
#     comment = get_object_or_404(Comment, id=pk, author=request.user)
#     if request.method == 'GET':
#         form = CommentForm(instance=comment)
#         return render(request, 'comments/comment_update.html', {'form': form, 'comment':comment})
#     elif request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment.save()
#             return redirect('questions:questions_detail', pk=comment.question_id)
#         else:
#             return render(request, 'comments/comment_update.html', {'form': form, 'comment': comment})
#
#
def new_comment(request):
    if request.method == 'GET':
        form = CommentForm()
        return render(request, 'comments/new_comment.html', {'form': form})
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        question_id = None
        try:
            question_id = int(request.GET.get('question_id'))
        except:
            redirect('core:index')

        try:
            comment_id = int(request.GET.get('prev_comment_id'))
        except:
            comment_id = None
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.question_id = question_id
            comment.comment_id = comment_id
            comment.author = request.user
            comment.save()
            return redirect('questions:questions_detail', pk=comment.question_id)
        else:
            return render(request, 'comments/new_comment.html', {'form': form})


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment.is_archive = True
    comment.save()
    return redirect('questions:questions_detail', pk=comment.question_id)


class ChangeComment(UpdateView):
    model = Comment
    fields = 'text',
    context_object_name = 'Comment'
    template_name = 'comments/comment_update.html'

    def get_success_url(self):
        return reverse('questions:questions_detail', kwargs={'pk': self.object.question.pk})
