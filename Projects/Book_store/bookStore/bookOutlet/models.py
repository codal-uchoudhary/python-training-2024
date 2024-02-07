from django.db import models

# Create your models here.

class Country(models.Model):
    name= models.CharField(max_length=50)


class Address(models.Model):
    #country = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True)
    state = models.CharField(max_length=50)

    def full_address(self):
        return f"{self.country} : {self.state}"
    
    def __str__(self):
        return self.full_address()
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address= models.OneToOneField(Address, on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name() 


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating=models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    published_country=models.ManyToManyField(Country)
    

    def __str__(self):
        return f"{self.title} and rating is ({self.rating})"
