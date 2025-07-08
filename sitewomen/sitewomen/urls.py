from django.contrib import admin
from django.urls import path, include
from women import views

urlpatterns = [
    path('/admin', admin.site.urls),
    path('/index', views.index),
    path('/categories', views.categories)
]
