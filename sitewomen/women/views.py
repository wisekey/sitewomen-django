from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render 
from django.shortcuts import get_object_or_404, redirect
from .models import Category, Women, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
from typing import Any


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
    data: dict[str, Any] = {
            'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", mode="wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request: HttpRequest):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data["file"])
            fp.save()
    else:
        form = UploadFileForm()

    context =  {
        "title": 'О сайте',
        "menu": menu,
        "form": form
    }

    return render(request, 'women/about.html', context)


def show_post(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Women, slug=post_slug)

    data: dict[str, Any] = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "cat_selected": 1 
    }

    return render(request, 'women/post.html', context=data)


def addpage(request: HttpRequest):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect("home")
            # except:
            #     form.add_error(None, "Ошибка добавления поста")
            form.save()
            return redirect("home")
    else:
        form = AddPostForm()
             
    data: dict[str, Any] = {'menu': menu,
            'title': 'Добавление статьи',
            'form': form,
    }

    return render(request, 'women/addpage.html', context=data)


def contact(request: HttpRequest):
    return HttpResponse("Контакты")


def login(request: HttpRequest):
    return HttpResponse("Логин")


def show_category(request: HttpRequest, cat_slug: str):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat__id=category.pk).select_related('cat')

    data: dict[str, Any] = {
            'title': f'Рубрика: {category.name}',
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk,
    }
    return render(request, "women/index.html", data)


def show_tag_postlit(request: HttpRequest, tag_slug: str):
    tag: TagPost = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    
    data: dict[str, Any] = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)

def page_not_found(request: HttpRequest, exception: Http404) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page Not Found</h1>")
