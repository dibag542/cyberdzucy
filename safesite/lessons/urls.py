from django.urls import path
from . import views

urlpatterns = [
    path('lessons', views.lesson, name='lesson'),
    path('lesson1', views.lesson1, name='lesson1'),
    path('lesson2', views.lesson2, name='lesson2'),
    path('lesson3', views.lesson3, name='lesson3')
]
