from django.db import models

# Create your models here.


class color(models.Model):
    color_name = models.CharField(max_length=30)


class Users(models.Model):
    username = models.CharField(max_length=40)
    age = models.IntegerField(null="True")
    color = models.ForeignKey(color, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
