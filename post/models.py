from django.db import models
from topic.models import AbstractModel, Topic


###
# Post Model
###


class Post(AbstractModel):
    content = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')