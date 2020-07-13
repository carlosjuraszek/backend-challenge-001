from django.http import Http404, HttpResponseBadRequest
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from post.api.v1.serializers import PostSerializer
from post.models import Post
from post.permissions import IsOwnerOrReadOnly
from topic.models import Topic
from comment.models import Comment



###
# Post ViewSet
###


class PostViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, update and delete a post inside one topic.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        for post in response.data['results']:
            post['comments'] = post['comments'][:3]

        return response

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    def perform_create(self, serializer):
        topic_url_name = self.kwargs.get('topics_url_name', None)

        try:
            topic = Topic.objects.get(url_name=topic_url_name)
        except Topic.DoesNotExist:
            raise HttpResponseBadRequest()

        serializer.save(author=self.request.user, topic=topic)

    def get_queryset(self):
        topic_url_name = self.kwargs.get('topics_url_name', None)
        try:
            topic = Topic.objects.get(url_name=topic_url_name)
        except Topic.DoesNotExist:
            raise Http404()

        qs = super().get_queryset()

        try:
            post = qs.filter(topic_id=topic.id)
            return post
        except Post.DoesNotExist:
            return Post.objects.none()