from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def whatif(request):
    return render(request, 'main/whatif.html')


def test(request):
    return render(request, 'main/test.html', {'test': test})


def interesting(request):
    return render(request, 'main/interesting.html', {'interesting': interesting})


