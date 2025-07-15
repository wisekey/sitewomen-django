from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from .models import Category, Women, TagPost

menu = [
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


def index(request: HttpRequest) -> HttpResponse:
    posts = Women.published.all().select_related('cat')
    data = {
            'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    return render(request, 'women/about.html', {'title': 'О сайте', "menu": menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "cat_selected": 1 
    }

    return render(request, 'women/post.html', context=data)


def addpage(request):
    return HttpResponse("Добавления статьи")


def contact(request):
    return HttpResponse("Контакты")


def login(request):
    return HttpResponse("Логин")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat__id=category.pk).select_related('cat')

    data = {
            'title': f'Рубрика: {category.name}',
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk,
    }
    return render(request, "women/index.html", data)


def show_tag_postlit(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)

def page_not_found(request: HttpRequest, exception: Http404) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page Not Found</h1>")
