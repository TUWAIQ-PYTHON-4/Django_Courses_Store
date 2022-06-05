from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Order'

urlpatterns = [
                  # path('cart_summary/', views.cart_summary, name='cart_summary'),
                  # path('add_to_cart/', views.add_to_cart, name='add_to_cart')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
