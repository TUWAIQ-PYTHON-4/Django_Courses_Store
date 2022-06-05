from django.urls import path
from . import views

app_name = "Store"
urlpatterns = [
    path('', views.Home, name='Home'),
    path('add-course/', views.Add_Course, name='Add_Course'),
    path('course-detail/', views.Course_Detail, name='Course_Detail'),
    path('orders/', views.Orders, name='Orders'),
    path('register/', views.Register, name='Register'),
    path('login/', views.Login, name='Login'),

]
