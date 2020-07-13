from django.urls import path
from . views import CommentViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from post.urls import post_nested_router


comment_nested_router = routers.NestedSimpleRouter(
    post_nested_router, r"posts", lookup="post"
)
comment_nested_router.register(r'comments', CommentViewSet, basename='comments')

