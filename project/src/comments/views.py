# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.shortcuts import reverse, get_object_or_404, redirect, HttpResponse
from .models import Comment
from questions.models import Question
from django.views.generic import CreateView, UpdateView


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'text',


class NewComment(CreateView):
    model = Comment
    fields = 'text',
    context_object_name = 'Comment'
    template_name = 'comments/new_comment.html'

    def get_context_data(self, **kwargs):
        context = super(NewComment, self).get_context_data(**kwargs)
        comment_id = 0
        if self.comment is not None:
            comment_id = self.comment.id
        context["question_id"] = self.question.id
        context["comment_id"] = comment_id
        context["comment"] = self.comment
        return context

    def dispatch(self, request, *args, **kwargs):
        question_id = None
        try:
            question_id = int(kwargs[u'q_id'])
        except:
            redirect('core:index')
        try:
            comment_id = int(kwargs[u'com_id'])
            self.comment = get_object_or_404(Comment, pk=comment_id)
        except:
            self.comment = None
        self.question = get_object_or_404(Question, pk=question_id)
        return super(NewComment, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = self.question
        form.instance.comment = self.comment
        super(NewComment, self).form_valid(form)
        return HttpResponse("OK")

    def get_success_url(self):
        return reverse('core:lk')
        # return self.request.META['HTTP_REFERER']
        # return reverse('questions:questions_detail', kwargs={'pk': self.question.id})


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
# def new_comment(request):
#     if request.method == 'GET':
#         form = CommentForm()
#         return render(request, 'comments/new_comment.html', {'form': form})
#     elif request.method == 'POST':
#         form = CommentForm(request.POST)
#         question_id = None
#         try:
#             question_id = int(request.GET.get('question_id'))
#         except:
#             redirect('core:index')
#
#         try:
#             comment_id = int(request.GET.get('prev_comment_id'))
#         except:
#             comment_id = None
#         if form.is_valid():
#             comment = Comment(text=form.cleaned_data['text'])
#             comment.question_id = question_id
#             comment.comment_id = comment_id
#             comment.author = request.user
#             comment.save()
#             return redirect('questions:questions_detail', pk=comment.question_id)
#         else:
#             return render(request, 'comments/new_comment.html', {'form': form})


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment.is_archive = True
    comment.save()
    return redirect('questions:questions_detail', pk=comment.question_id)


class ChangeComment(UpdateView):
    model = Comment
    fields = 'text',
    context_object_name = 'comment'
    template_name = 'comments/comment_update.html'

    def form_valid(self, form):
        super(ChangeComment, self).form_valid(form)
        return HttpResponse("OK")

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']
        # return reverse('questions:questions_detail', kwargs={'pk': self.object.question.pk})
