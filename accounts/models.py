from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    img=models.ImageField(upload_to='user_img',default='user_img/prof.jpg')
    phone=models.IntegerField(null=True)