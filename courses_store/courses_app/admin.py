from django.contrib import admin
from .models import *

class CoursesAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    list_display = ('user', 'title', 'duration', 'price', 'start_date')
    list_filter = ('online', 'price')
    search_fields = ('title','user')

class ReviewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('user', 'course', 'rating')
    list_filter = ('course',)
    search_fields = ('course',)

class OrdersAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('user', 'course', 'total_price')




admin.site.register(Courses, CoursesAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Orders, OrdersAdmin)
