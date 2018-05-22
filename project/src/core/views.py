# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from questions.models import Question
from django.conf import settings
from django.views.generic.edit import FormView
from forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from comments.models import Comment
from django.views.generic import UpdateView
from models import User


class Login(LoginView):
    template_name = "core/login.html"


class Logout(LogoutView):
    template_name = "core/logout.html"


def index(request):
    questions = Question.objects.filter(is_archive=False).order_by('-created')
    resent_questions = []
    if questions.count() > 5:
        for i in range(5):
            resent_questions.append(questions[i])
    else:
        resent_questions = questions

    answers = Comment.objects.filter(is_archive=False, comment=None).order_by('-created')
    resent_answered_questions = []
    # if answers.count() > 5:
    #     for i in range(5):
    #         resent_answered_questions.append(answers[i].question)
    # else:
    #     for answer in answers:
    #         resent_answered_questions.append(answer.question)

    i = 0
    for answer in answers:
        if i >= 5:
            break
        if answer.question not in resent_answered_questions:
            resent_answered_questions.append(answer.question)
            i += 1

    context = {
        'resent_questions': resent_questions,
        'resent_answered_questions': resent_answered_questions
    }
    return render(request, 'core/index.html', context)


def log_in(request):
    return Login.as_view()


def log_out(request):
    return Logout.as_view()


def lk(request):
    context = {
        'questions': Question.objects.all().filter(is_archive=False, author=request.user).order_by('-created')
    }
    return render(request, 'core/lk.html', context)


# class RegisterFormView(FormView):
#     form_class = CustomUserCreationForm
#     success_url = settings.LOGIN_URL
#
#     template_name = "core/register.html"
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)

class UpdateUser(UpdateView):
    model = User
    fields = 'first_name', 'last_name', 'email', 'avatar'
    context_object_name = 'core'
    template_name = 'core/settings.html'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def get_object(self, **kwargs):
        return get_object_or_404(User, pk=self.request.user.id)


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect(settings.LOGIN_URL)
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': user_form})


# def user_configurations(request):
#     if request.method == 'POST':
#         user_form = PasswordChangeForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         user_form = PasswordChangeForm(user=request.user)
#     return render(request, 'core/change_password.html', {'form': user_form})


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('core:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'core/change_password.html', {
        'form': form,
    })
