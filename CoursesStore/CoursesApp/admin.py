from django.contrib import admin
from .models import Course, Review,Order

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price','online')
    date_hierarchy = 'start_date'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'date', 'totalprice')

admin.site.register(Course, CourseAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)