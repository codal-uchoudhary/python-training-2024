from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating=models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(null=True,max_length=50)
    

    def __str__(self):
        return f"{self.title} and rating is ({self.rating})"
