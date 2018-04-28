from django.conf.urls import url

from comments import views as comment_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^(?P<pk>\d+)/$',  question_views.question_detail, name='questions_detail'),
    url(r'^(?P<pk>\d+)/change$', login_required(comment_views.ChangeComment.as_view()), name='comment_change'),
    url(r'^new/$', login_required(comment_views.new_comment), name='new_comment'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(comment_views.delete_comment), name='delete_comment'),
]
