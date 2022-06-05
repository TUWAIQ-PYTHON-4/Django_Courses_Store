from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    # path("add_movie_perm/", views.add_movie_permission, name="add_movie_perm"),
    # path("add_to_group_editors/", views.add_to_group_editors, name="add_to_group_editors"),
]