from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from articleapp.models import Ingridient, Food


class IngridientListView(ListView):
    model = Ingridient
    context_object_name = 'ingridient_list'
    template_name = 'articleapp/ingri_list.html'
    paginate_by = 30

class FoodListView(ListView):
    model = Food
    context_object_name = 'food_list'
    template_name = 'articleapp/food_list.html'
    paginate_by = 30


