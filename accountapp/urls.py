from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world

app_name ="accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
