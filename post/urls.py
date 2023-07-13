from django.urls import path
from . import views
app_name = "PostModel"
urlpatterns = [
    path("", views.main_view, name="index"),
    path("about/", views.about_view, name="about"),
    path("post/", views.list_view_post, name="post"),
]