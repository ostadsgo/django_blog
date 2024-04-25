from django.contrib.auth.models import User
from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)



STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f"{self.title}"
