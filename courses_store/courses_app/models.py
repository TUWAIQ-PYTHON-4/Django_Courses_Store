from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 25)
    description = models.TextField()
    duration = models.IntegerField(help_text = 'how many days it will take')
    price = models.DecimalField(max_digits = 5, decimal_places=2)
    image = models.ImageField(upload_to="images/courses_img")
    online = models.BooleanField(help_text = 'is it online or offline')
    start_date = models.DateTimeField(auto_now = False, auto_now_add = False)

    def __str__(self):
        return f'{self.title}'


class Reviews(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits = 1,decimal_places=0, help_text = 'the product rating from 0 - 10')
    date = models.DateTimeField(auto_now_add = True)
    comment = models.TextField()

    def __str__(self):
        return f'{self.user.username} {self.course.title} {self.rating}'


class Orders(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now = False, auto_now_add = False)
    total_price = models.DecimalField(max_digits = 5, decimal_places=2)
    # method to calc tax in view before asigning val

    def __str__(self):
        return f'{self.course.title} {self.total_price}'
