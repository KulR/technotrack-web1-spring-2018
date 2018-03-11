# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def categories(request):

    return HttpResponse("You're on the categories page")

def category(request, number):

    return HttpResponse("You're on the {} category page".format(number))
