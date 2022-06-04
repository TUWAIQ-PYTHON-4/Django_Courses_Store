from django.contrib import admin

from django.contrib import admin
from .models import Course, Review,Order


admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Order)