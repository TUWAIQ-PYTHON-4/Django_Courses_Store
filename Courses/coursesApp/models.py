from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=20)
    descr = models.TextField()
    duration = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    online = models.BooleanField()
    start_date = models.DateField()
    user = models.IntegerField(User)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    totale_price = models.FloatField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course)
