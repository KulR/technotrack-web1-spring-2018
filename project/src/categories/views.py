# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category
from .forms import CategoriesListForm


def category_list(request):
    form = CategoriesListForm(request.GET)
    categories = Category.objects.all().filter(is_archive=False)
    if form.is_valid():
        if form.cleaned_data['sort']:
            categories = categories.order_by(form.cleaned_data['sort'])
        if form.cleaned_data['search']:
            categories = categories.filter(name__icontains=form.cleaned_data['search'])
    categories_list = []
    for category in categories:
        category.questions_qs = category.questions.filter(is_archive=False)
        categories_list.append(category)
    context = {
        'category_list_form': form,
        'categories': categories_list,
    }
    return render(request, 'categories/categories_list.html', context)


def category_detail(request, pk):

    category = get_object_or_404(Category, id=pk)
    questions = category.questions.all().filter(is_archive=False)
    # comment_list = []
    # for question in questions:
    #     question.likes_qs = comment.likes.filter(is_archive=False)
    #     comment.liked = 0
    #     if request.user.id is not None:
    #         comment.liked = comment.likes.filter(is_archive=False, author=request.user).count()
    #     comment_list.append(comment)
    context = {
        'category': category,
        'questions': questions,
    }
    return render(request, 'categories/category_detail.html', context)


def category_change(request, pk):

    return HttpResponse("You change the {} category page".format(pk))
