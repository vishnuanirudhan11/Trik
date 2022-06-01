from django.db import models
from cart.models import cart_id
import datetime
# Create your models here.

class loginstats(models.Model):
    user=models.ForeignKey(cart_id,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.date.today)
    home=models.IntegerField()

class aboutus(models.Model):
    about=models.TextField()
    terms_cond=models.TextField()