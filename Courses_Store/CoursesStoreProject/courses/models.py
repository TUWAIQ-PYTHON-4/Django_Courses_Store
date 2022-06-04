from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    duration: models.TextField()
    price = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='Courses/images/')
    online = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    totalprice = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
