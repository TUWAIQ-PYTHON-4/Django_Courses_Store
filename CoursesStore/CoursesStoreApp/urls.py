from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<course_id>", views.detail, name="detail"),
    path("orders/", views.orders, name="orders"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("add/", views.add_Course, name="add_Course"),
    path(" ", views.display_review, name="display_review"),
    path("add_review/<review_id>", views.add_review, name="add_review"),
    path("add_course_perm/", views.add_course_permission, name="add_course_perm"),
    path("add_to_group_editors/", views.add_to_group_editors, name="add_to_group_editors"),
]
