from django.urls import path
from . import views


urlpatterns = [
     path('', views.home,name='home'),
     path("add/", views.add_course, name="add_course"),
     path("detail/<course_id>", views.course_detail, name="course_detail"),
     path("register/", views.register_user, name="register"),
     path("login/", views.login_user, name="login"),
     path("add_course_perm/", views.add_course_permission, name="add_course_perm"),
 ]