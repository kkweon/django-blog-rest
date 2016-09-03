from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]


'''
data = {
    "title": "yeah",
    "content": "new content",
    "publish": "2016-01-02",
    "slug": "yeah-buddy"
}
new_item = PostSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
'''
