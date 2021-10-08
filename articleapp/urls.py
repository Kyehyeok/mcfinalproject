from django.urls import path
from django.views.generic import TemplateView

from articleapp import views
from articleapp.views import IngredientListView, FoodListView, IngredientBuyView

app_name ="articleapp"

urlpatterns = [
    path('ingredient_list/', IngredientListView.as_view(), name='ingredient'),
    path('food_list/', FoodListView.as_view(), name='food'),
    path('ingredient_buy/', IngredientBuyView.as_view(), name='ingredient_buy'),
# path('ingredient_buy/', views.result, name='ingredient_buy'),
]
