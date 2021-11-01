from django.forms import ModelForm

from articleapp.models import Ingredient, Food, FoodDetail, IngredientUnique, Mealkit, Starpoint


class IngredientListForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['code','ingredient','price','subscribe','bigcat','smallcat','imageurl','quantity','keyword','weight','url']

class FoodListForm(ModelForm):
    class Meta:
        model = Food
        fields = ['code','name','ingredient','quantity','keyword']

class FoodDetailListForm(ModelForm):
    class Meta:
        model = FoodDetail
        fields = ['code','name','recipe']

class IngredientUniqueListForm(ModelForm):
    class Meta:
        model = IngredientUnique
        fields = ['code','bigcat','keyword']

class MealkitListForm(ModelForm):
    class Meta:
        model = Mealkit
        fields = ['code', 'ranking', 'mealkit', 'product', 'thumbnail', 'price', 'brand', 'url', 'review_cnt']

class StarpointForm(ModelForm):
    class Meta:
        model = Starpoint
        fields = ['user','post_food','star_point']
