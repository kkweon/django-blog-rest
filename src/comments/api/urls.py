from django.conf.urls import url

from comments.api.views import CommentDetailAPIView, CommentListAPIView, CommentDeleteAPIView

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    url(r'^(?P<id>\d+)/$', CommentDeleteAPIView.as_view(), name='delete'),
]
