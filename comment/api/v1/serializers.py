from rest_framework import serializers
from comment.models import Comment



###
# Comment Serializer
###

class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['id', 'content']