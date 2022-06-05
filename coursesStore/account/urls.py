from django.urls import  path
from . import views

urlpatterns = [
    path('register/',views.reigester,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),

]