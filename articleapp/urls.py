from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import AAAA

app_name ="articleapp"

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('AAAA/', AAAA, name='AAAA'),
]
