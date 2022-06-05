import imp
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField()
    online = models.BooleanField()
    start_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)

    #def total_price(self):
    #    total = self.course.price * 1.15
    #    return total

    total_price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return str(self.id)