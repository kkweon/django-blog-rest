from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'content',
            'timestamp',
            'reply_count',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()

        return 0


class CommentChildSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
        ]

    def get_user(self, obj):
        if obj.user is not None:
            return obj.user.username
        return None


class CommentDetailSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    replies = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'content',
            'reply_count',
            'replies',
        ]

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()

        return 0
