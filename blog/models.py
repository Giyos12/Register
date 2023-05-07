from django.db import models
from auth2.models import Student
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="PB")


class Post(models.Model):
    choice = (
        ("DF", "Draft"),
        ("PB", "Published")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, choices=choice, default='DF')

    objects = models.Manager()  # default
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]

    def __str__(self):
        return self.title


