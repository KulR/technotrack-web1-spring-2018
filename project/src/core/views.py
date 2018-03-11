# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def hellopage(request):
    return HttpResponse("Hello, mister!")


def index(request):
    return render(request, 'core/index.html')


def log_in(request):
    name = request.GET.get('name')
    return HttpResponse("Hello {}".format(name))


def log_out(request):
    return HttpResponse("You loged out. Goodbye!")
