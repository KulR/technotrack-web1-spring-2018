from django.conf.urls import url, include

from likes import views as likes_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^comment/(?P<pk>\d+)$', login_required(likes_views.CreateLikeComment), name='comment'),
    url(r'^question/(?P<pk>\d+)$', login_required(likes_views.CreateLikeQuestion), name='question'),
    url(r'^delete$', login_required(likes_views.CreateLikeComment), name='delete'),

]
