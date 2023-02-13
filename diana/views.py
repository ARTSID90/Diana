from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *


menu = ["О сайте", "Модель", "Контакты"]
def index(request):
    posts = Diana.objects.all()
    return render(request, 'diana/index.html', {'post': posts, 'menu': menu, 'title': 'Главная страница'})
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')