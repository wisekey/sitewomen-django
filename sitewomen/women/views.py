from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def index(request: HttpRequest) -> HttpResponse:
    data = {
            'title': 'Главная страница',
            'menu': menu,
            "float": 28.56,
            "lst": [1, 2, 'abc', True],
            "set": {1, 2, 3, 5},
            "dict": {'key_1': "value_1", 'key_2': "value_2"},
            "obj": MyClass(1, 2, 3),
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id : {cat_id}</p>")


def categories_by_slug(request: HttpRequest, cat_slug: str) -> HttpResponse:
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request: HttpRequest, year: int) -> HttpResponse:
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>Год издания: {year}</p>")


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("О сайте")


def catalog(request: HttpRequest) -> HttpResponse:
    return HttpResponse("catalog")


def page_not_found(request: HttpRequest, exception: Http404) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page Not Found</h1>")


def post_detail(request: HttpRequest) -> HttpResponse:
    if request.GET:
        return HttpResponse("|".join(f"{k}={v}" for k, v in request.GET.items()))
    return HttpResponse("GET is empty")

