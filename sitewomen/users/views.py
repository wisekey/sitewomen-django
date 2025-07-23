from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "users.login.html"
    extra_context = {"title": }

def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd["username"],
                password=cd["password"]
            )
            
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
    else:
        form = LoginUserForm()    

    return render(request, "users/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))