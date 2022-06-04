from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userApp/',include('userApp.urls')),
    path('', include('coursesstorApp.urls'))

]
