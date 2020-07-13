from rest_framework import serializers
from topic.models import Topic
from post.api.v1.serializers import PostSerializer


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    posts = PostSerializer(many=True, read_only=True)
    url_name = serializers.ReadOnlyField()

    class Meta:
        model = Topic
        fields = ['id', 'author', 'name', 'title',
                  'description', 'url_name', 'posts']

