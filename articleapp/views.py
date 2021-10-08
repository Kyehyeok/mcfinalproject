
# Create your views here.
from django.http import request
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from articleapp.models import Ingredient, Food, FoodDetail

class IngredientListView(ListView):
    model = Ingredient
    context_object_name = 'ingredient_list'
    template_name = 'articleapp/ingredient_list.html'
    paginate_by = 30


class FoodListView(ListView):
    model = Food
    context_object_name = 'food_list'
    template_name = 'articleapp/food_list.html'
    paginate_by = 30


    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(FoodListView, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['food_detail_list'] = FoodDetail.objects.all()
        return context

class FoodDetailListView(ListView):
    model = FoodDetail
    context_object_name = 'food_detail_buy'
    # template_name = 'articleapp/ingredient_buy.html'
    paginate_by = 30

class IngredientBuyView(ListView):
    model = Ingredient
    context_object_name = 'ingredient_buy'
    template_name = 'articleapp/ingredient_buy.html'

    def post(self, request):
        ingredient_list = Ingredient.objects.all()
        check = request.POST.getlist('checks[]')
        return render(request, 'articleapp/ingredient_buy.html', {'check_ingre': check, 'ingre_list': ingredient_list})
