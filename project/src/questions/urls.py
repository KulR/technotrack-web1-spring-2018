from django.conf.urls import url, include
from django.contrib import admin

from questions import views as question_views

urlpatterns = [
    url(r'^list/$', question_views.question_list, name='questions_list'),
    url(r'^(?P<pk>\d+)/detail$', question_views.question_detail, name='questions_detail.html'),
#    url(r'^(?P<pk>\d+)/change$', question_views.change_question, name='question_change'),
        ]
