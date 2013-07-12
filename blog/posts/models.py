from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

import misaka
from model_utils import Choices
from model_utils.models import StatusModel


class Post(StatusModel):
    STATUS = Choices('draft', 'live')
    title = models.CharField(max_length=2048)
    slug = models.SlugField(max_length=2048)
    excerpt = models.TextField(blank=True)
    excerpt_html = models.TextField(blank=True, editable=False)
    content = models.TextField()
    content_html = models.TextField(blank=True, editable=False)
    created_at = models.DateTimeField(blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()

        if self.excerpt:
            self.excerpt_html = misaka.html(self.excerpt)
        self.content_html = misaka.html(self.content)

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})
