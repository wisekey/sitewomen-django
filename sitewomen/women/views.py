from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Category, Women, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
from .utils import DataMixin
from typing import Any
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class WomenHome(DataMixin, ListView):
    model = Women
    template_name = "women/index.html"
    context_object_name = "posts"
    title_page = "Главная страница"
    cat_selected = 0

    def get_queryset(self):
        return Women.published.all().select_related("cat")


@login_required
def about(request: HttpRequest):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request, 'women/about.html', {
        "title": "О сайте",
        "page_obj": page_obj
    })


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context["post"].title)
     
    
    def get_object(self, queryset = None):
        return get_object_or_404(
            Women.published,
            slug=self.kwargs[self.slug_url_kwarg]
        )


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = "women/addpage.html"
    title_page = "Добавление статьи"

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(UpdateView):
    model = Women
    fields = ["title", "content", "photos", "cat"]
    template_name = "women/addpage.html"
    success_url = reverse_lazy("home")
    title_page = "Обновление статьи"
    extra_object_name = ""


def contact(request: HttpRequest):
    return HttpResponse("Контакты")


def login(request: HttpRequest):
    return HttpResponse("Логин")


class WomenCategory(DataMixin, ListView):
    """
    Класс реализует обработку вывода женщин по категория.
    """
    model = Women
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

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

        return self.get_mixin_context(
            context,
            title=f"Категория - {cat.name}",
            cat_selected=cat.pk
        )
    

class TagPostList(DataMixin, ListView):
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

        return self.get_mixin_context(context, title=f"Тег - {tag.tag}")


def page_not_found(request: HttpRequest, exception: Http404) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page Not Found</h1>")
