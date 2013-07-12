from django import template

from ..models import Post

register = template.Library()


@register.inclusion_tag('posts/partials/_list.html')
def show_posts(num=5):
    return {'posts': Post.live.all()[:num]}
