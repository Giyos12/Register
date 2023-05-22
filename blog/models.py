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


class Commit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Comments by {self.name} on {self.post}'


# bugungi yangilikla id =1
# commit = Commit.objects.get(id=1)
# commit.post # bugungi yanilikla

# post = Post.objects.get(id=1)
# commits = Commit.objects.filter(post=post)  # queryset['']
# commits = Post.objects.get(id=1).comment.all()
