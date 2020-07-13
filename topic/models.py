from django.db import models
from django.utils.text import slugify


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE)


class Topic(AbstractModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url_name = models.SlugField(unique=True)

    def generate_slug(self, title):
        slug_candidate = slugify(title)
        existing_topic = Topic.objects.filter(url_name=slug_candidate)

        index = 0
        while len(existing_topic) != 0:
            slug_candidate = slugify(title + "-" + str(index))
            existing_topic = Topic.objects.filter(url_name=slug_candidate)
            index += 1
        return slug_candidate

    def save(self, *args, **kwargs):
        self.url_name = self.generate_slug(self.title)
        super(Topic, self).save(*args, **kwargs)