from django.shortcuts import render

# Create your views here.
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

    # def get_queryset(self):
    #     self.publisher = get_object_or_404(Publisher, name=self.args[0])
    #     return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(FoodListView, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['food_detail_list'] = FoodDetail.objects.all() #.select_related().order_by('-code')
        return context

class FoodDetailListView(ListView):
    model = FoodDetail
    context_object_name = 'food_detail_list'
    template_name = 'articleapp/food_list.html'
    paginate_by = 30

