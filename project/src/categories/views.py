# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404
from .models import Category


def category_list(request):
    categories = get_list_or_404(Category)
    #categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'categories/categories_list.html', context)

def category_detail(request, pk):

    category = get_object_or_404(Category, id=pk)
    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False),
    }
    return render(request, 'categories/category_detail.html', context)

def category_change(request, pk):

    return HttpResponse("You change the {} category page".format(pk))
