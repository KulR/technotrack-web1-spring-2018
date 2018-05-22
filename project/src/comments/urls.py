from django.conf.urls import url

from comments import views as comment_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/change$', login_required(comment_views.ChangeComment.as_view()), name='comment_change'),
    # url(r'^new/q_id_(?P<q>\d+)/com_id_(?P<com>\d+)$', login_required(comment_views.new_comment), name='new_comment'),
    url(r'^new/q_(?P<q_id>\d+)/com_(?P<com_id>\d+)$', login_required(comment_views.NewComment.as_view()),
        name='new_comment'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(comment_views.delete_comment), name='delete_comment'),
]
