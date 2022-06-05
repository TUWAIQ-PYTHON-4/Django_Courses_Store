from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name='home'),
                  path('course_detail<int:id>', views.course_detail, name='course_detail'),
                  path('orders<int:id>', views.orders_detail, name='orders'),
                  path('add_course', views.add_course, name='add_course'),
                  path('add_review<int:id>', views.add_review, name='add_review'),
                  path('order_course/<int:id>', views.order_course, name='order_course'),
                  path('show_detail', views.show_detail, name='show_detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
