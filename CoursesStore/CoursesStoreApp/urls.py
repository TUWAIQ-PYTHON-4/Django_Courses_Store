from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

app_name = 'CoursesStoreApp'

urlpatterns = [
                  path('home/', views.home, name='home'),
                  path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
                  path('register/', views.register, name='register'),
                  path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
