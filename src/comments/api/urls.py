from django.conf.urls import url

from comments.api.views import (
    CommentDetailAPIView,
    CommentListAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
)

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    url(r'^(?P<id>\d+)/edit/$', CommentUpdateAPIView.as_view(), name='update'),
    # url(r'^(?P<id>\d+)/delete/$', CommentDeleteAPIView.as_view(), name='delete'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
]
