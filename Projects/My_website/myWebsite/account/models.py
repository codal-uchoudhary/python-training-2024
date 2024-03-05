from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserContent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bookmarks = models.ManyToManyField(Post, related_name="bookmark_list")
