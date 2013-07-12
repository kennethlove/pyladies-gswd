from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list_view(request):
    return render(request, 'posts/post_list.html', {
        'post_list': Post.objects.all()
    })


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_detail.html', {
        'post': post
    })
