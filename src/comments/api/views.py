from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from comments.api.serializers import CommentSerializer, CommentDetailSerializer, create_comment_serializer, \
    CommentUpdateSerializer
from comments.models import Comment
from posts.api.pagination import PostPagePagination


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        model_type = self.request.GET.get('type')
        slug = self.request.GET.get('slug')
        parent_id = self.request.GET.get('parent_id', None)

        return create_comment_serializer(
            model_type=model_type,
            slug=slug,
            parent_id=parent_id,
            user=self.request.user,
        )


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


class CommentUpdateAPIView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentUpdateSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

