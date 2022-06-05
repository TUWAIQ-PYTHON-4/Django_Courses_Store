from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ditail/<int:course_id>', views.course_ditail, name='ditail'),
    path('newcourse/',views.CourseCreateView.as_view(),name='newcourse'),
]
