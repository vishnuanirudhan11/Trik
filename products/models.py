from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class productstable(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='products')
    categ=models.ForeignKey(category,on_delete=models.CASCADE)
    offers=models.BooleanField(default=False)
    offerprice=models.IntegerField()
    avilability=models.BooleanField(default=True)

    def __str__(self):
        return self.name

