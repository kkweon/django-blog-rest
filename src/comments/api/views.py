from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from comments.api.serializers import CommentSerializer, CommentDetailSerializer, create_comment_serializer, \
    CommentListSerializer
from comments.models import Comment
from posts.api.pagination import PostPagePagination
from posts.api.permissions import IsOwnerOrReadOnly


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

class CommentListAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter
    ]
    search_fields = [
        'content',
        'user__first_name',
        'user__username',
    ]
    lookup_field = 'id'

    pagination_class = PostPagePagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.filter(id__gte=0)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list


class CommentDetailAPIView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

