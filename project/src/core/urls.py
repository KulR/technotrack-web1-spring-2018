from django.conf.urls import url, include
from django.contrib import admin

from core import views as core_views

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^login$', core_views.log_in, name='login'),
    url(r'^logout$', core_views.log_out, name='logout'),
    url(r'^lk/$', core_views.lk, name='lk'),
    url(r'^hello/$', core_views.hellopage, name='hello'),
]
