from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views




urlpatterns = [
    path("", views.index, name="index"),
    path('detail/<course_id>',views.detail,name='detail'),
    path("add/", views.add, name="add"),
    path('orders/<course_id>',views.buy,name='orders'),
    path("buy/", views.buy, name="buy"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)