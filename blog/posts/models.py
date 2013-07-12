from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=2048)
    slug = models.SlugField(max_length=2048)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

