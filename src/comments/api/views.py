from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from comments.api.serializers import CommentSerializer, CommentDetailSerializer
from comments.models import Comment
from posts.api.pagination import PostPagePagination


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'


class CommentDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter
    ]
    search_fields = [
        'content'
    ]
    lookup_field = 'id'

    pagination_class = PostPagePagination
