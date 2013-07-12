from django.http import Http404
from django.shortcuts import render

from .models import Post


def post_list_view(request):
    return render(request, 'posts/post_list.html', {
        'post_list': Post.live.all()
    })


def post_detail_view(request, slug):
    try:
        post = Post.live.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("That post doesn't exist")

    return render(request, 'posts/post_detail.html', {
        'post': post
    })
