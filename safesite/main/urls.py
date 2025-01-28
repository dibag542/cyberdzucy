from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('whatif', views.whatif, name='whatif'),
    path('test', views.test, name='test'),
    path('interesting', views.interesting, name='interesting')
]
