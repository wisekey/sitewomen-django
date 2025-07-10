from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

menu_dict = [
    {
        "title": "О сайте",
        "urlpath": "about"
    },
    {
        "title": "Добавить статью",
        "urlpath": "add_page"
    },
    {
        "title": "Обратная связь",
        "urlpath": "contact"
    },
    {
        "title": "Войти",
        "urlpath": "login"
    }
]


posts = [
    {
        "id": 1,
        "title": "Как начать изучать Python",
        "content": "Python — это мощный и гибкий язык программирования, который подходит как для новичков, так и для опытных разработчиков. В этой статье мы рассмотрим основные шаги, которые помогут вам начать изучение Python.",
        "is_published": True
    },
    {
        "id": 2,
        "title": "10 советов по продуктивности для программистов",
        "content": "Программирование может быть сложным и требовать много времени. В этой статье мы собрали 10 советов, которые помогут вам повысить свою продуктивность и лучше управлять своим временем.",
        "is_published": True
    },
    {
        "id": 3,
        "title": "Лучшие библиотеки для анализа данных на Python",
        "content": "Python предлагает множество библиотек для анализа данных, таких как Pandas, NumPy и Matplotlib. В этой статье мы рассмотрим, как использовать эти библиотеки для эффективного анализа данных.",
        "is_published": False
    },
    {
        "id": 4,
        "title": "Основы веб-разработки с использованием Flask",
        "content": "Flask — это легкий веб-фреймворк для Python, который позволяет быстро создавать веб-приложения. В этой статье мы рассмотрим основные концепции и примеры использования Flask.",
        "is_published": True
    },
    {
        "id": 5,
        "title": "Как работать с API на Python",
        "content": "Работа с API — важный навык для разработчиков. В этой статье мы обсудим, как использовать библиотеки, такие как Requests, для взаимодействия с API на Python.",
        "is_published": False
    }
]


def index(request: HttpRequest) -> HttpResponse:
    data = {
            'title': 'Главная страница',
            'menu': menu_dict,
            'posts': posts,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    return render(request, 'women/about.html', {'title': 'О сайте', "menu": menu_dict})


def show_post(request, post_id):
    return HttpResponse(f"Отображние статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавления статьи")


def contact(request):
    return HttpResponse("Контакты")


def login(request):
    return HttpResponse("Логин")


def page_not_found(request: HttpRequest, exception: Http404) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page Not Found</h1>")



