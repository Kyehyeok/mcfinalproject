from django.forms import ModelForm

from articleapp.models import Article

class IngredientListForm(ModelForm):
    class Meta:
        model = Article
        fields = ['ingri','price','subscribe','bigcat','smallcat','imageurl','quantity','keyword']

