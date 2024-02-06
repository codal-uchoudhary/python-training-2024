from django.db import models




class Tag(models.Model):
    caption = models.CharField(max_length = 20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title=models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=30)
    data = models.DateField(auto_now=True)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    author = models.ForeignKey(Author,null=True,on_delete = models.SET_NULL,related_name = "posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
