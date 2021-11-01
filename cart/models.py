from django.db import models

# Create your models here.
from django.db import models
from articleapp.models import Ingredient, Mealkit

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank= True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']
    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product_ingre = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    product_mealkit = models.ForeignKey(Mealkit, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    activate = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        cart_ingre =self.product_ingre.price * self.quantity
        cart_mealkit= self.product_mealkit.price * self.quantity
        return {'cart_ingre': cart_ingre, 'cart_mealkit': cart_mealkit}

    def __str__(self):
        return self.product_ingre, self.product_mealkit