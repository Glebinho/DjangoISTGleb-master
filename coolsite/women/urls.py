from django.urls import path, register_converter

from women.classurl import FourDigitYearConverter

from women.views import *

register_converter(FourDigitYearConverter,"yyyyy")

urlpatterns = [
    path('',index),
    path('cat/',categories),
    path("articles/<yyyyy:year>/",year_archive)
   

]