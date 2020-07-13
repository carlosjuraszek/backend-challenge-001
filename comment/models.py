from django.db import models
from topic.models import AbstractModel
from post.models import Post


###
# Comment Model
###

class Comment(AbstractModel):
    content = models.TextField()
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)