from django.shortcuts import render

# Create your views here.
from articleapp.models import Article


def AAAA(request):
    ingri_list = Article.objects.all()
    return render(request, 'articleapp/list.html', context={'ingri_list':ingri_list})

