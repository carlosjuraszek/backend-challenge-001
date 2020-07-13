from rest_framework import viewsets, permissions
from rest_framework.response import Response
from topic.api.v1.serializers import TopicSerializer
from topic.models import Topic
from topic.permissions import IsOwnerOrReadOnly


class TopicViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, update and delete a topic.
    """

    lookup_field = 'url_name'
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        for topic in response.data['results']:
            topic['posts'] = topic['posts'][:3]

            for post in topic['posts']:
                del post['comments']

        return response

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)