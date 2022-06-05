from django.urls import path
from . import views

app_name = "CoursesStoreApp"

urlpatterns = [
    path("", views.home, name="home"),
    path("add_course/", views.add_course, name="add_course"),
    path('detail/<course_id>', views.course_detail, name='detail'),

]