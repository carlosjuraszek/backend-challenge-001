from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers
from topic.api.v1 import views
from post.api.v1.views import PostViewSet
from comment.api.v1.views import CommentViewSet

###
# Nested Routes:  topics/{url_name}/posts/{post_id}/comments/{comments_id}
###

router = routers.DefaultRouter()
router.register(r'topics', views.TopicViewSet)

topic_post_router = routers.NestedSimpleRouter(
    router, r'topics', lookup='topics')
topic_post_router.register(r'posts', PostViewSet, basename='posts')

post_comment_router = routers.NestedSimpleRouter(
    topic_post_router, r'posts', lookup='posts')
post_comment_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(topic_post_router.urls)),
    url(r'^', include(post_comment_router.urls)),
]