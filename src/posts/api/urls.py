from django.conf.urls import url

from posts.api.views import PostListAPIView, PostDetailAPIView, PostDeleteAPIView, PostUpdateAPIView

urlpatterns = [
   url(r"^$", PostListAPIView.as_view(), name='list'),
   url(r"^(?P<slug>[\w-]+)/$", PostDetailAPIView.as_view(), name='detail'),
   url(r"^(?P<slug>[\w-]+)/edit/$", PostUpdateAPIView.as_view(), name='update'),
   url(r"^(?P<slug>[\w-]+)/delete/$", PostDeleteAPIView.as_view(), name='delete'),
   #url(r"^(?P<pk>\d+)/$", PostDetailAPIView.as_view(), name='detail'),
]