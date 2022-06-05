from django.urls import path
from . import views




urlpatterns = [

    path('', views.index, name="index"),
    path('add_course', views.add_course, name='add_course'),
    path('detail/<course_id>', views.course_detail, name='detail'),
    path('orders/<course_id>',views.buy,name='orders'),

]