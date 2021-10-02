from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    code = models.CharField(max_length=20, null=True)
    ingredient = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=10, null=True)
    subscribe = models.CharField(max_length=100, null=True)
    bigcat = models.CharField(max_length=10, null=True)
    smallcat = models.CharField(max_length=20, null=True)
    imageurl = models.CharField(max_length=200, null=True)
    quantity = models.CharField(max_length=10, null=True)
    keyword = models.CharField(max_length=10, null=True)

class FoodDetail(models.Model):
    # code = models.ForeignKey('Food', on_delete=models.SET_NULL, related_name='article', null=True)
    code = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    ingredient = models.CharField(max_length=20, null=True)
    quantity = models.CharField(max_length=20, null=True)

class Food(models.Model):
    code = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
