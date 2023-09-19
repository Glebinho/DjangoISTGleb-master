from django.http import HttpResponse
from django.shortcuts import render
#для хранения представлений(контролеры) текущего приложения
# Create your views here.

def index(request):
    return HttpResponse('главная страница women')

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')

def termin(request):
    return HttpResponse('<i>Термины</i>')
def top(request):
    return HttpResponse('<h2>Победа</h2>')
