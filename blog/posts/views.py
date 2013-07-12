from django.shortcuts import render

from .models import Post


def post_list_view(request):
    return render(request, 'posts/post_list.html', {
        'post_list': Post.objects.all()
    })

