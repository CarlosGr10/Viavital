from django.shortcuts import render
from .models import PostModel


def list_view_post(request):
    the_list = PostModel.objects.all()
    context = {'the_list': the_list}
    return render(request, "post.html", context)

def about_view(request):
    return render(request, "about.html")
