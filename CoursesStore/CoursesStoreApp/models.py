import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()  # check
    price = models.FloatField()
    image = models.ImageField(upload_to="images")
    online = models.BooleanField()  # check (is it online or offline , boolean)
    start_date = models.DateTimeField(datetime.date)


    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])
    comment = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # check
    date = models.DateTimeField(auto_now_add=True)
    totalprice = models.FloatField()  # check  Course.price (the course price + tax)

    def __str__(self):
        return self.totalprice
