
# Create your views here.
import json

import pandas as pd

from django.http import request
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from articleapp.models import Ingredient, Food, FoodDetail, Mealkit, IngredientUnique


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
        # 모든 쿼리 집합을 context 객체에 추가한다.
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


class MealkitBuyView(ListView):
    model = Mealkit
    context_object_name = 'mealkit_buy'
    template_name = 'articleapp/mealkit_buy.html'
    paginate_by = 30

    def post(self, request):
        mealkit_list = Mealkit.objects.all()
        check = request.POST.get('check_mealkit')
        return render(request, 'articleapp/mealkit_buy.html', {'check_mealkit': check,'mealkit_list':mealkit_list})

class MyFridgeView(ListView):
    model = IngredientUnique
    context_object_name = 'fridge_list'
    template_name = 'articleapp/my_fridge.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        posts = IngredientUnique.objects.all()
        context = {
            "posts_js": json.dumps([post.to_json() for post in posts])
        }
        return context
    # def post(self, request, *argc, **kwargs):
    #     unique_list = IngredientUnique.objects.all()
    #     ingredient_list = Ingredient.objects.all()
    #     check_cat = request.POST.get('category')
    #     check_ingre = request.POST.getlist('ingredient[]')
    #
    #     return render(request, 'articleapp/my_fridge.html',{'category':check_cat, 'ingre_list': ingredient_list, 'unique_list':unique_list ,'check_ingre': check_ingre })

class RecommendView(ListView):
    model = FoodDetail
    context_object_name = 'fooddetail'
    template_name = 'articleapp/recommend.html'

    def post(self, request):
        food_detail_list=FoodDetail.objects.all()
        fooddetail_value = FoodDetail.objects.all().values()
        fooddetail_df=pd.DataFrame(fooddetail_value).copy()

        reco = request.POST.getlist('reco[]')

        input_list = set(reco)
        sub_list = ['소금', '후추', '간장', '마요네즈', '설탕', '물', '올리브오일', '민트잎', '꿀', '허브', '항귀', '바질', '레몬즙']
        ranking_list = []

        recipe_list_df = fooddetail_df.set_index('name').groupby('name').agg(lambda x: x.tolist())
        for i in range(len(recipe_list_df)):
            recipe_ingred = set(recipe_list_df['ingredient'][i])
            require_ingred = (recipe_ingred - input_list)
            exist_ingred = (recipe_ingred & input_list)

            temp_require = list(exist_ingred)

            sub_ingred_list = []
            main_ingred_list = []
            for k in range(len(temp_require)):
                if temp_require[k] in sub_list:
                    sub_ingred_list.append(temp_require[k])
                else:
                    main_ingred_list.append(temp_require[k])

            try:
                score = ((len(main_ingred_list) * 2) + len(sub_ingred_list)) / len(recipe_ingred)
            except:
                score = 0

            ranking_list.append({
                "name": recipe_list_df.index[i],
                "exist_ingred": list(exist_ingred),
                "require_ingred": list(require_ingred),
                "score": score
            })
            result = sorted(ranking_list, key=lambda x: (-x['score']))[:5]

        return render(request, 'articleapp/recommend.html', {'reco': reco, 'food_detail_list': food_detail_list, 'result':result})

