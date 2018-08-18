from django.conf.urls import url, include
from django.contrib import admin

from core import views as core_views
from django.contrib.auth.decorators import login_required
from models import *

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^login$', core_views.Login.as_view(), name='login'),
    url(r'^logout$', login_required(core_views.Logout.as_view()), name='logout'),
    url(r'^lk/$', login_required(core_views.lk), name='lk'),
    url(r'^register/$', core_views.register, name='register'),
    url(r'^settings/$', login_required(core_views.UpdateUser.as_view()), name='settings'),
    url(r'^change_password/$', login_required(core_views.change_password), name='change_password'),
]
