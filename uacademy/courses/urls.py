from argparse import Namespace
from django.urls import path
from . import views

Namespace = 'courses'

urlpatterns = [
     path('', views.courses, name='courses'),
     path('courses/<course_id>', views.course_details,name='course_details'),
     path('add_course', views.add_course, name='add_course'),
     path('add_order/<order_id>', views.add_order, name='add_order'),
]