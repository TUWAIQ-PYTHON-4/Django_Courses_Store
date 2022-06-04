from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=224)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    online = models.BooleanField()
    start_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.rating)

class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    totalprice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return str(self.totalprice)