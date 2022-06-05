from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('course_detail/<str:course_id>', views.course_detail, name='course_detail'),
    path('course_form', views.course_form, name='course_form'),
    path('Orders/<str:course_id>', views.Orders, name='Orders'),
    path('display_orders', views.display_orders, name='display_orders'),
    path('checkout', views.checkout, name='checkout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)