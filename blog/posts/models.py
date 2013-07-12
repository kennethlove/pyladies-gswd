from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def live(self):
        return self.get_query_set().filter(status=True)


class Post(models.Model):
    title = models.CharField(max_length=2048)
    slug = models.SlugField(max_length=2048)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)
    status = models.BooleanField(default=True)

    objects = PostManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        super(Post, self).save(*args, **kwargs)
