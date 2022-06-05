from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'Course'

urlpatterns = [
                  path('', views.all_courses, name='all_courses'),
                  path('course_detail/<id>/', views.course_detail, name='course_detail'),
                  path('cart_summary/', views.cart_summary, name='cart_summary'),
                  path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
                  path('search_course', views.search_course, name='search_course'),
                  path('my_orders', views.my_orders, name='my_orders'),
                  path('add_course', views.add_course, name='add_course'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
