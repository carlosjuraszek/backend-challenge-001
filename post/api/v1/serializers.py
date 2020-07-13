from rest_framework import serializers
from post.models import Post
from comment.api.v1.serializers import CommentSerializer

###
# Post Serializer 
###

class PostSerializer(serializers.ModelSerializer):
    topic = serializers.ReadOnlyField(source='topic.id')
    author = serializers.ReadOnlyField(source='author_id')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'topic', 'title',
                  'content', 'author', 'comments']