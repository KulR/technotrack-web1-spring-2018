from django.conf.urls import url, include
from django.contrib import admin

from questions import views as question_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^list/$', question_views.question_list, name='questions_list'),
    url(r'^(?P<pk>\d+)/$',  question_views.question_detail, name='questions_detail'),
    url(r'^(?P<pk>\d+)/comments$', question_views.question_comments, name='question_comments'),
    url(r'^(?P<pk>\d+)/change$', login_required(question_views.ChangeQuestion.as_view()), name='question_change'),
    url(r'^new/$', login_required(question_views.NewQuestion.as_view()), name='new_question'),
    url(r'^(?P<pk>\d+)/delete$', login_required(question_views.delete_question), name='delete_question'),
]
