from django.shortcuts import render
from .models import PostModel


def main_view(request):
    return render(request, "start.html")


def list_view_post(request):
    the_list = PostModel.objects.all()
    recent_post = PostModel.objects.all().order_by('-created')[:5]
    context = {'posts': the_list, 'recent_posts': recent_post}
    return render(request, "post.html", context)


def about_view(request):
    recent_post = PostModel.objects.all().order_by('-created')[:10]
    context = {'recent_posts': recent_post}
    return render(request, "about.html", context)
