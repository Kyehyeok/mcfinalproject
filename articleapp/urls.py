from django.urls import path
from django.views.generic import TemplateView

# from articleapp import views
from articleapp.views import IngredientListView, FoodListView, IngredientBuyView, MealkitBuyView, MyFridgeView, \
    RecommendView

app_name ="articleapp"

urlpatterns = [
    path('ingredient_list/', IngredientListView.as_view(), name='ingredient'),
    path('food_list/', FoodListView.as_view(), name='food'),
    path('ingredient_buy/', IngredientBuyView.as_view(), name='ingredient_buy'),
    path('mealkit_buy/', MealkitBuyView.as_view(), name='mealkit_buy'),
    path('my_fridge/',MyFridgeView.as_view(), name='my_fridge'),
    path('recommend/',RecommendView.as_view(), name='recommend'),
]
