from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import path, reverse_lazy
from . import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        views.LoginUser.as_view(),
        name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),
    
    path(
        "password-change/",
        views.UserPassowordChange.as_view(),
        name="password_change"
    ),
    path(
        "password-change/done/",
        PasswordChangeView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done"
    ),
    path(
        "password-reset/",
        PasswordResetView.as_view(
             template_name="users/password_reset_form.html"
        ),
        email_template_name="users/password_reset_email.html",
        name="password_reset",
        success_url=reverse_lazy("users:password_reset_done")
    ),
    path(
        "password-reset/done",
        PasswordResetDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_reset_done"
    ),
    
    path(
        'password-reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name='password_reset_confirm',
        success_url=reverse_lazy("users:password_reset_done")
    ),
    path(
        'password-reset/complete/',
        PasswordResetCompleteView.as_view(
             template_name="users/password_reset_complete.html"
        ),
        name='password_reset_complete'
    ),
    
    path(
        "register/",
        views.RegisterUser.as_view(),
        name="register"
    ),
    path(
        "profile/",
        views.ProfileUser.as_view(),
        name="profile"
    )
]