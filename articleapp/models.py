from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ingridient(models.Model):

    ingri = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=10, null=True)
    subscribe = models.CharField(max_length=100, null=True)
    bigcat = models.CharField(max_length=10, null=True)
    smallcat = models.CharField(max_length=20, null=True)
    imageurl = models.CharField(max_length=200, null=True)
    quantity = models.CharField(max_length=10, null=True)
    keyword = models.CharField(max_length=10, null=True)

class Food(models.Model):
    name = models.CharField(max_length=20, null=True)
    ingridient = models.CharField(max_length=200, null=True)
