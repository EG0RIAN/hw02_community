from django.shortcuts import get_object_or_404, render

from .models import Post, Group

from .settings import POST_PER_PAGE


def index(request):
    posts = (
        Post.objects
        .settings.POST_PER_PAGE
    )
    context = {'posts': posts, }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = (
        Post.objects.filter(group=group)
        .order_by('-pub_date').POST_PER_PAGE
    )

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
