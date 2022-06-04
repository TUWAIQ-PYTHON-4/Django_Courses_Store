import datetime

from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=124)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images")
    online = models.BooleanField()
    start_date = models.DateTimeField(datetime.date)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])
    comment = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    totalprice = models.FloatField()

    def __str__(self):
        return self.course
