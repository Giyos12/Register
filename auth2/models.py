from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.hashers import make_password


# Create your models here.

class Student(AbstractUser):
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    # USERNAME_FIELD = phone_number

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Token(models.Model):
    token = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)

# student = Student.objects.get(id=1)
# posts = Post.objects.filter(author=student)
#
# posts = Student.blog_post.all()
