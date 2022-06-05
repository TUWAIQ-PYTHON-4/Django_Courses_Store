from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Order :
# course (the course to order)
# user (the user who ordered the course)
# date (when was the order)
# totalprice (the course price + tax)


# class Order(models.Model):
#     course = models.ForeignKey('Course.Course', on_delete=models.DO_NOTHING)
#     customer = models.ForeignKey('CoursesStoreApp.Customer', on_delete=models.CASCADE, null=True, blank=True)
#     date = models.DateTimeField(auto_now=True)
#     totalprice = models.IntegerField()
#
#     def __str__(self):
#         return str(self.course)


# class Cart(models.Model):
#     customer = models.ForeignKey('CoursesStoreApp.Customer', on_delete=models.CASCADE, null=True, blank=True)
#     date = models.DateTimeField(auto_now=True)
#

# class CartItem(models.Model):
#     course = models.ForeignKey('Course.Course', on_delete=models.DO_NOTHING)
#     totalprice = models.FloatField(blank=True)
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     Tax = 1.50
#
#     def price_ttc(self):
#         total = self.totalprice * (1 + self.Tax / 100.0)
#         return str(total)
#
#     def __str__(self):
#         return self.course
