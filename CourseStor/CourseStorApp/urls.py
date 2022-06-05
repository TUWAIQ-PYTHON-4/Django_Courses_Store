from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("detail", views.detail, name="detail"),
    path("order", views.order, name="order"),
    path("add", views.add, name="add"),
    path("checkout", views.checkout, name="checkout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
