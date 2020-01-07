from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# one to many releationshp

# Create your models here.
# Database is here
# Users and posts


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # if user deleated we want to deleate post but if we deleate post we dont deleate user

    def __str__(self):
        return self.title
