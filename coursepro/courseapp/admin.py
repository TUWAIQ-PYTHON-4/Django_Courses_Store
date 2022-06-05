from django.contrib import admin
from .models import course

class courseAdmin(admin.ModelAdmin):
    pass

admin.site.register(course, courseAdmin)
