from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name='home'),
    path('details/<course_id>' , views.course_details,name='details'),
    path("add/", views.add, name="add"),
    #path("orders/<course_id>", views.orders, name="orders"),
    path("course_details/<course_id>",views.course_details,name="course_details"),
    #path("buy_orders/<course_id>", views.buy_orders, name="buy_orders"),
    path("order1/", views.order1,name="order"),
    path("add_order/<course_id>", views.add_order, name="add_order"),
    #path("signup", views.signup, name='signup')
    path("register/", views.user_register, name='user_register'),
    path("dashboard", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('search/ ', views.search, name="search")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)