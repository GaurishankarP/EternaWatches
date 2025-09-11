from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view,logout_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Password reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="auth_app/password_reset.html",
            email_template_name="auth_app/password_reset_email.html",
            subject_template_name="auth_app/password_reset_subject.txt",
            success_url=reverse_lazy("password_reset_done"),
            # from_email="no-reply@yourdomain.com",  # optional
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth_app/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth_app/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth_app/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
