from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the women's index")


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Статьи по категориям</h1>")