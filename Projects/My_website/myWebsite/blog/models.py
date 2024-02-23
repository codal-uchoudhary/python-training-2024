from django.db import models
from django.contrib.auth.models import User




class Tag(models.Model):
    caption = models.CharField(max_length = 20)

    def __str__(self):
        return self.caption




class Post(models.Model):
    title=models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.ImageField(upload_to='static/blog/',null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    author = models.ForeignKey(User,null=True,on_delete = models.SET_NULL,related_name = "posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
