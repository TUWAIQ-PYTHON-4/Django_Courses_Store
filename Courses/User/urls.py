from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('login_user', views.login_user, name='login'),
                  path('register_user', views.register_user, name='register_user'),
                  path('logout_user', views.logout_user, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
