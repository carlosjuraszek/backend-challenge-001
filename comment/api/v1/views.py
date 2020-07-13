from django.http import Http404, HttpResponseBadRequest
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from comment.models import Comment
from comment.api.v1.serializers import CommentSerializer
from comment.permissions import IsOwnerOrReadOnly
from post.models import Post
from topic.models import Topic


###
# Comment ViewSet
###

class CommentViewSet(viewsets.ModelViewSet):
    
    """
    List, create, retrieve, update and delete a comment inside a post.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        topic_url_name = self.kwargs.get('topics_url_name', None)
        post_id = self.kwargs.get('posts_pk')
        qs = super().get_queryset()

        try:
            topic = Topic.objects.get(url_name=topic_url_name)
        except Topic.DoesNotExist:
            raise Http404()

        try:
            comment = qs.all().filter(post_id=post_id)
        except Comment.DoesNotExist:
            return Comment.objects.none()

        return comment

    def perform_create(self, serializer):
        try:
            post = Post.objects.get(pk=self.kwargs.get('posts_pk'))
        except Post.DoesNotExist:
            raise HttpResponseBadRequest()

        serializer.save(author=self.request.user,
                        post=post)