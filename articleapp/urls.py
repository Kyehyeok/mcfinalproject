from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import IngredientListView, FoodListView, FoodDetailListView

app_name ="articleapp"

urlpatterns = [
    path('ingredient_list/', IngredientListView.as_view(), name='ingredient'),
    # path('food_list/', FoodDetailListView.as_view(), name='food_detail'),
    path('food_list/', FoodListView.as_view(), name='food'),

]
