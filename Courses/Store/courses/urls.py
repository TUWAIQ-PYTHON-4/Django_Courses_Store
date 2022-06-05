from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('', views.home, name='home'),
    path('detail/<course_id>', views.details, name='detail'),
    path('add/', views.add, name='add'),
    path('order/<course_id>', views.buy, name='order'),
    path('getMyOrders/', views.getMyOrders, name='getMyOrders')

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)