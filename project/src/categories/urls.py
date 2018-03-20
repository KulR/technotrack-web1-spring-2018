from django.conf.urls import url, include
from django.contrib import admin

from categories import views as categories_views

urlpatterns = [
    url(r'^list/$', categories_views.category_list, name='category_list'),
    url(r'^(?P<pk>\d+)/detail$', categories_views.category_detail, name='category_detail'),
    #url(r'^categories/(?P<pk>\d+)/change$', categories_views.category_change, name='category_change'),
        ]
