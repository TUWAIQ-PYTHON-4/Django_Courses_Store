
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("register/",views.register, name="register"),
]