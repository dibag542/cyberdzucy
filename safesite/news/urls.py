from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('fishing', views.fishing, name='fishing'),
    path('register', views.register, name='register'),
    path('register1', views.register1, name='register1'),
    path('register2', views.register2, name='register2'),
    path('register3', views.register3, name='register3'),
    path('noregister', views.noregister, name='noregister'),
    path('noregister1', views.noregister1, name='noregister1'),
    path('noregister2', views.noregister2, name='noregister2')
]
