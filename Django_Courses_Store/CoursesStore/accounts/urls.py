from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("add_perm", views.add_permission, name="add_perm"),
    path("add_to_group", views.add_to_group, name="add_to_group"),
]