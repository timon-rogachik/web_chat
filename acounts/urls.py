from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from acounts.forms import RegisterForm
from acounts.views import *
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name="profile"),
    path(
        'register/',
        RegistrationView.as_view(
            success_url=reverse_lazy('main'),
            form_class=RegisterForm), name="register"
    ),
    path('', include("django_registration.backends.one_step.urls")),
    path('', include("django.contrib.auth.urls")),
    ]