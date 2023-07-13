from django.urls import path
from . import views
app_name = "PostModel"
urlpatterns = [
    path("", views.list_view_post, name="index"),
    path("about/", views.about_view, name="about"),
]