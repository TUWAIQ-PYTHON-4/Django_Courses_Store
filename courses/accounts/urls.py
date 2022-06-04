from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("add_post_perm/", views.add_post_permission, name="add_post_perm"),

]