from django.contrib import admin

from .models import Course, Order, Review, CartOrderItems


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'course', 'rating', 'comment',)
    list_filter = ('customer', 'course', 'rating',)
    search_fields = ('customer', 'course', 'rating',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'price', 'image', 'online', 'start_date',)
    list_filter = ('start_date', 'online',)
    search_fields = ('start_date', 'online',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('course', 'customer', 'date', 'totalprice',)
    list_filter = ('course',)
    search_fields = ('course',)


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'image', 'price', 'total',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Review, ReviewAdmin)

