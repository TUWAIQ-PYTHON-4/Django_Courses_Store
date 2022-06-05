from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_course/", views.add_course, name="add_course"),
    path("course_detail/<course_id>", views.course_detail, name="course_detail"),
    path("course_orders/<course_id>", views.course_orders, name="course_orders")

]