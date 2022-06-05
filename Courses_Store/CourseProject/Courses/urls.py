from django.urls import path
from . import views
urlpatterns = [path('', views.base, name='base'),
               path('AddCourses/', views.AddCourses, name='AddCourses'),
                path('home/', views.home, name='home'),
               path('detail/<course_id>', views.course_detail, name='detail'),
               path('orders/<course_id>', views.buy, name='orders'),

               ]