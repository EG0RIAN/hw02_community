from django.shortcuts import get_object_or_404, render

from .models import Group, Post

POST_PER_PAGE = 10


def index(request):
    posts = (
        Post.objects.all()[:POST_PER_PAGE]
    )
    context = {'posts': posts, }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = (
        Post.objects.filter(group=group)[:POST_PER_PAGE]
    )

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
