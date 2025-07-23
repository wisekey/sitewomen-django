from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}
    
    
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {
        "tutle": "Регистрация"
    }
    success_url = reverse_lazy("users:login")
