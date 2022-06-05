from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.list_course,name='home'),
    path('add/',views.add_course,name='add'),
    path('post/<pk>', views.comment_detile, name='course'),
    path('orders/<course_id>',views.buy,name='orders'),
    path('my_order',views.orders,name='my_orders'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)