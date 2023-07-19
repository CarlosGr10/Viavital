from django.shortcuts import render, get_object_or_404
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


def detail_post(request, detail_id):
    data = get_object_or_404(PostModel, pk=detail_id)
    context = {"data": data}
    return render(request, "detail_post.html", context)