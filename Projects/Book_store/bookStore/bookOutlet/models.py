from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating=models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return f"{self.title} and rating is ({self.rating})"
