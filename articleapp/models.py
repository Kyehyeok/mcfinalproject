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
    weight = models.IntegerField(default=3, null=True)
    url = models.CharField(max_length=200, null=True)

class FoodDetail(models.Model):
    # code = models.ForeignKey('Food', on_delete=models.SET_NULL, related_name='article', null=True)
    code = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    ingredient = models.CharField(max_length=20, null=True)
    quantity = models.CharField(max_length=20, null=True)
    keyword = models.CharField(max_length=20, null=True)


class Food(models.Model):

    code = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    recipe = models.CharField(max_length=1000, null=True)

class Mealkit(models.Model):
    code = models.CharField(max_length=20, null=True)
    ranking = models.CharField(max_length=20, null=True)
    mealkit = models.CharField(max_length=50, null=True)
    product = models.CharField(max_length=20, null=True)
    thumbnail = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=20, null=True)
    url = models.CharField(max_length=200, null=True)
    review_cnt = models.CharField(max_length=20, null=True)


class IngredientUnique(models.Model):
    code = models.CharField(max_length=20, null=True)
    bigcat = models.CharField(max_length=20, null=True)
    keyword = models.CharField(max_length=20, null=True)

    def to_json(self):
        return {
            "code": self.code,
            "bigcat": self.bigcat,
            "keyword": self.keyword
        }

class Starpoint(models.Model):
    user = models.CharField(max_length=20, null=True)
    post_food = models.CharField(max_length=20, null=True)
    star_point = models.IntegerField(default=3, null=True)

    # def __int__(self):
    #     return self.star