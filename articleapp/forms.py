from django.forms import ModelForm

from articleapp.models import Ingredient, Food, FoodDetail, IngredientUnique


class IngredientListForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['code','ingredient','price','subscribe','bigcat','smallcat','imageurl','quantity','keyword']

class FoodListForm(ModelForm):
    class Meta:
        model = Food
        fields = ['code','name','ingredient','quantity']

class FoodDetailListForm(ModelForm):
    class Meta:
        model = FoodDetail
        fields = ['code','name']

class IngredientUniqueListForm(ModelForm):
    class Meta:
        model = IngredientUnique
        fields = ['code','bigcat','keyword']
