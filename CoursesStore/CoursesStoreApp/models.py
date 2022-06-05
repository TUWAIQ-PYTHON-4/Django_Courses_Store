from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="images")
    online = models.BooleanField()
    start_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
