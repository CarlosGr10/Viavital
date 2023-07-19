from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    photo = models.ImageField(upload_to='posts/photos')
    summary = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

