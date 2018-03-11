# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def questions(request):
    return HttpResponse("You're on the questions page")


def question(request, number):
    #    change = request.GET.get('change')
    #    if change == "1":
    #        return HttpResponse("You're change {} question".format(number))
    #    else:
    return HttpResponse("You're on the {} question page".format(number))


def change_question(request, number):
    return HttpResponse("You're change {} question".format(number))
