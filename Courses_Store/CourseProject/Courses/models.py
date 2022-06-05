from django.contrib.auth.models import User
from django.db import models


class courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField()
    duration = models.IntegerField()
    online = models.BooleanField()

    def __str__(self):
        return self.title
    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rate = models.CharField(max_length=100)
    comment = models.TextField(max_length=112)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.rate


class Order(models.Model):
    courses = models.ForeignKey(courses, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()

    def __str__(self):
        return self.total_price
