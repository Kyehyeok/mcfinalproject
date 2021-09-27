from django.forms import ModelForm

from articleapp.models import Ingridient, Food


class IngredientListForm(ModelForm):
    class Meta:
        model = Ingridient
        fields = ['ingri','price','subscribe','bigcat','smallcat','imageurl','quantity','keyword']

class IngredientListForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name','ingridient']
