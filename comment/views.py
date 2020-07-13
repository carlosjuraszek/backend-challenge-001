from django.shortcuts import render
from comment.models import Comment
from comment.serializers import CommentSerializer
from rest_framework import generics, permissions, viewsets
from accounts.api.v1.permissions import IsOwnerOrReadOnly


###
# Comment Viewset
###

class CommentViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'comment_id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)