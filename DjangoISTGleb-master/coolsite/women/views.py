from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, \
    HttpResponseServerError
from django.shortcuts import render, redirect
#для хранения представлений(контролеры) текущего приложения
# Create your views here.
from women.classurls import FourDigitYearConverter

#Классная работа

def index(request):
    print(request.GET)
    data={'title': 'Главная страница',
          'slov':{"key1": "value_1", "key2": "value_2"},
          'int':{"key1":5,"key2":37},
          'double':{"key1":14.7,"key2":45.056},
          'bool':{"key1":False,"key2":True},
          }
    #return HttpResponse('главная страница women')
    return render(request, 'women/index.html', context=data)
def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')

def categories_id(request, catid):
    if 30 < catid < 60:
        return redirect('home')
    elif 60 < catid < 90:
        return redirect('home', permanent=True)
    elif 90 < catid < 110:
        return redirect('cat_slug', 'dfdfdf')
    return HttpResponse(f'<h1>Статьи по номерам  {catid} </h1>')

def categories_sl(request, catid):
    return HttpResponse(f'<h1>Статьи по названиям и категориям  {catid} </h1>')

#ДЗ №1 список группы

dir = {
'1': ['Буренок Д. 2005'],
'2': ['Горбанёв К. 2006'],
'3': ['Капшукова Д. 2004'],
'4': ['Климин Т. 2004'],
'5': ['Кашаева Р. 2004'],
'6': ['Косенков Г. 2004'],
'7': ['Костин М. 2001'],
'8': ['Кузенков Б. 2003'],
'9': ['Миколодзе А. 2004'],
'10': ['Мишин А. 2004'],
'11': ['Мишин А. 2004'],
'12': ['Сентюрина Е. 2002'],
'13': ['Пешеходько А. 2004'],
}

def students(request, students_id):
    if students_id > 0 and students_id <= 10:
        return HttpResponse(f"<h1>Студент {students_id}){dir[str(students_id)][0]} найден</h1>")

    else:

        return HttpResponse(f"<h1>Студента под номеромом {students_id} нет</h1>")
def students_slug(request, students):
    return HttpResponse(f"<h1>Статья про студента{students}</h1>")
def spisok(request,key):
    return HttpResponse(f"<h1> Список участников № {dir[key]} </h1>")


def date(request,datee):
    dir = {
"2001": ['Костин М.'],
"2002": ['Сентюрина Е.'],
"2003": ['Кузенков Б.'],
"2004": ['Капшукова Д.','Климин Т.','Кашаева Р.','Косенков Г.','Миколодзе А.','Мишин А.','Мишин А.','Пешеходько А.'],
"2005": ['Буренок Д.'],
"2006": ['Горбанёв К.'],

}
    if datee > 2000 and datee < 2007:
        return HttpResponse(f"<h1> Студенты {dir[str(datee)]} найдены </h1>")
    else:
        return HttpResponse(f"<h1>Студента с таким годом {datee} нет</h1>")

#ДЗ №2 Get запрос
def get_page(request):
    if(request.GET):
        result = str()
        for key in request.GET:
            result += key + ": " + request.GET[key] + ", "
        return HttpResponse(f"<h2>Get-запрос</h2> <p>Запрос: {result}</p>")
#ДЗ № 3 Ошибки
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')
def badRequest(request, exception):
    return HttpResponseBadRequest(f"Bad Request")

def forbiden(request, exception):
    return HttpResponseForbidden(f"Forbiden")

def serverError(request, exception):
    return HttpResponseServerError('serverError')

def year(request, year):
    if year > 2000 or year < 2023:
        return HttpResponse(f"<h1> год  {year} победа русских </h1>")

#Дз redirect
def Win(request,pobeda):
    if 11 < pobeda < 20:
        return redirect('home')
    elif 2000 < pobeda < 23:
        return redirect('home', permanent=True)
    elif 23 < pobeda < 50:
        return redirect('students', 6)

