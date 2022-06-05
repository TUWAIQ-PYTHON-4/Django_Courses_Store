from django.urls import path
from . import views

app_name = "Accounts"

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    #path("add_course_perm/", views.add_course_permission, name="add_course_perm"),
]