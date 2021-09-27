from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import IngridientListView, FoodListView

app_name ="articleapp"

urlpatterns = [
    path('ingri_list/', IngridientListView.as_view(), name='ingri_list'),
    path('food_list/', FoodListView.as_view(), name='food_list'),
]
