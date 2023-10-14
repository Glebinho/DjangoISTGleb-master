from django.urls import path,register_converter

from women.classurls import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index),
    path('cat/', categories),
    path("articles/<yyyy:year>/",year),
    path('cat/<int:catid>/', categories_id),
    path('cat/<slug:catid>/', categories_id),
    path('students/<int:students_id>/', students),
    path('students/<slug:students>/', students_slug),
    path("spisok/<int:key> ",spisok),
    path('date/<int:datee>/',date),

]
