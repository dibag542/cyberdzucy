from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def fishing(request):
    return render(request, 'news/fishing.html', {'fishing': fishing})


def register(request):
    return render(request, 'news/register.html')


def register1(request):
    return render(request, 'news/register1.html')


def register2(request):
    return render(request, 'news/register2.html')


def register3(request):
    return render(request, 'news/register3.html')


def noregister(request):
    return render(request, 'news/noregister.html')


def noregister1(request):
    return render(request, 'news/noregister1.html')


def noregister2(request):
    return render(request, 'news/noregister2.html')