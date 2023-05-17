from django.db import models
from django.urls import reverse

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
    slug = models.SlugField(max_length=200, unique_for_date='publish')  # 2023/05/15/post1,post1
    author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())  # 2023/06/15/
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, choices=choice, default='DF')

    objects = models.Manager()  # default
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
