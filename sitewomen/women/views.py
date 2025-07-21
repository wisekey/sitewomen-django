from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render 
from django.shortcuts import get_object_or_404, redirect
from .models import Category, Women, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
from typing import Any
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView


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


class WomenHome(ListView):
    # model = Women
    template_name = "women/index.html"
    context_object_name = "posts"
    extra_context = {
            'title': 'Главная страница',
            'menu': menu,
            'cat_selected': 0,
    }

    def get_queryset(self):
        return Women.published.all().select_related("cat")


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


class ShowPost(DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update({
            "title": context["post"].title,
            "menu": menu
        })

        return context
    
    def get_object(self, queryset = None):
        return get_object_or_404(
            Women.published,
            slug=self.kwargs[self.slug_url_kwarg]
        )


class AddPage(View):
    def get(self, request):
        """
        Обрабатывает get-запрос и возвращает отображение пустой формы
        """
        form = AddPostForm()
        data: dict[str, Any] = {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form,
        }

        return render(request, 'women/addpage.html', context=data)

    def post(self, request):
        """
        Обрабатывает post-запрос и, после проверки на валидность данных
        формы сохраняет ее, далее перенаправляет на главную страницу. Если
        данные невалидны снова отображается форма
        """
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        
        data: dict[str, Any] = {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form,
        }

        return render(request, 'women/addpage.html', context=data)

def contact(request: HttpRequest):
    return HttpResponse("Контакты")


def login(request: HttpRequest):
    return HttpResponse("Логин")


class WomenCategory(ListView):
    """
    Класс реализует обработку вывода женщин по категория.
    """
    model = Women
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False
    paginate_by = 8

    def get_queryset(self):
        """
        Возвращает множество записей, фильтруя их по слагу, который берется
        из параметра запроса
        """
        return Women.published.filter(
            cat__slug=self.kwargs["cat_slug"]).select_related("cat")
    
    def get_context_data(self, **kwargs):
        """
        Передает данные в контекст для отображения
        """
        context = super().get_context_data(**kwargs)

        cat_slug = self.kwargs["cat_slug"]
        cat = get_object_or_404(Category, slug=cat_slug)

        context.update({
            "title": f"Категория - {cat.name}",
            "menu": menu,
            "cat_selected": cat.pk
        })
        
        return context


def show_tag_postlit(request: HttpRequest, tag_slug: str):
    tag: TagPostList = get_object_or_404(TagPostList, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    
    data: dict[str, Any] = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)


class TagPostList(ListView):
    model = TagPost
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        tag = get_object_or_404(TagPost, slug=self.kwargs["tag_slug"])
        return tag.tags.filter(
            is_published=Women.Status.PUBLISHED).select_related("cat")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs["tag_slug"])

        context["title"] = f"Тег - {tag.tag}"
        context["menu"] = menu
        context["cat_selected"] = None

        return context


def page_not_found(request: HttpRequest, exception: Http404) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page Not Found</h1>")
