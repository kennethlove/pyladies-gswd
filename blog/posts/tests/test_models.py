from django.test import TestCase

from ..models import Post


class PostModelTests(TestCase):
    def test_creation(self):
        post = Post.objects.create(
            title="my title",
            slug="my-slug",
            content="some content"
        )
        self.assertTrue(isinstance(post, Post))
