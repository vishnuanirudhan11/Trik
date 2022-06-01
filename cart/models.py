from django.db import models
from products.models import productstable

# Create your models here.

class cart_id(models.Model):
    session=models.CharField(max_length=100,unique=True,blank=True,null=True)
    userid=models.IntegerField(unique=True,null=True,blank=True)
    def __str__(self):
        return self.userid

class cartlist(models.Model):
    user=models.ForeignKey(cart_id,on_delete=models.CASCADE)
    productid=models.ForeignKey(productstable,on_delete=models.CASCADE)
    quantity=models.IntegerField()


class recent(models.Model):
    userid=models.ForeignKey(cart_id,on_delete=models.CASCADE)
    stats=models.BooleanField(default=True)
    date=models.DateField(null=True)