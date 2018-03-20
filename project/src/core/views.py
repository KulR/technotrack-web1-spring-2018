# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def hellopage(request):
    return HttpResponse("Hello, mister!")


def index(request):
    return render(request, 'core/index.html')


def log_in(request):
    return render(request, 'core/login.html')


def log_out(request):
    return render(request, 'core/logout.html')

def lk(request):
    context = {}
    return render(request, 'core/lk.html')
