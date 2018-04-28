# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from questions.models import Question
from django.conf import settings
from django.views.generic.edit import FormView
from forms import CustomUserCreationForm


class Login(LoginView):
    template_name = "core/login.html"


class Logout(LogoutView):
    template_name = "core/logout.html"


def index(request):
    return render(request, 'core/index.html')


def log_in(request):
    return Login.as_view()


def log_out(request):
    return Logout.as_view()


def lk(request):
    context = {
        'questions': Question.objects.all().filter(is_archive=False, author=request.user)
    }
    return render(request, 'core/lk.html', context)


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = settings.LOGIN_URL

    template_name = "core/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect(settings.LOGIN_URL)
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': user_form})
