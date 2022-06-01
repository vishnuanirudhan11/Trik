from django.db import models
from products.models import productstable
from cart.models import cart_id
import datetime
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class users(models.Model):
    seen=models.BooleanField(default=False)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)


class messages(models.Model):
    msgtxt=models.TextField()
    user=models.ForeignKey(cart_id,on_delete=models.CASCADE)
    trikmsg=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now=True)
    seen=models.ForeignKey(users,on_delete=models.CASCADE,null=True)


class comment(models.Model):
    productid=models.IntegerField()
    cmt=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)


class orders(models.Model):
    userid=models.IntegerField(null=True)
    prodid=models.ForeignKey(productstable,on_delete=models.CASCADE)
    session=models.CharField(max_length=50,blank=True)
    curstats=models.BooleanField(default=False)
    boughtprice=models.IntegerField()
    cancel=models.BooleanField(default=False)
    ordered_date=models.DateField(default=datetime.date.today)
    done_date=models.DateField(null=True)
    quan=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
