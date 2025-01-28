from django.shortcuts import render
from .models import Article
from django.views.generic import DetailView

def lesson(request):
    return render(request, 'lessons/lesson.html', {'lesson': lesson})

def lesson1(request):
    return render(request, 'lessons/lesson1.html', {'lesson1': lesson1})
def lesson2(request):
    return render(request, 'lessons/lesson2.html', {'lesson2': lesson2})
def lesson3(request):
    return render(request, 'lessons/lesson3.html', {'lesson3': lesson3})

