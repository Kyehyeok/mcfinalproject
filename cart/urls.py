from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name ="cart"

urlpatterns = [
    path('add/<int:product_id>/', views.add_ingre_cart, name='add_ingre_cart'),
    path('',views.cart_detail, name='cart_detail'),
]