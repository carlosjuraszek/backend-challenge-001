from . models import Comment
from rest_framework import serializers

# Comment Serializer 

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'post', 'title', 'content', 'created_at', 'updated_at']