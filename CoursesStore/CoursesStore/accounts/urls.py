from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("add_course_permission/", views.add_course_permission, name="add_course_permission"),
    path("add_to_group_managers/", views.add_to_group_managers, name="add_to_group_managers"),
]