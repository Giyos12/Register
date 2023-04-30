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
