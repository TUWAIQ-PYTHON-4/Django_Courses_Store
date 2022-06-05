from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='course/photos/', null=True, blank=True)
    online = models.BooleanField()
    start_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']


class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    totalprice = models.FloatField()

    def __str__(self):
        return str(self.course)


class CartOrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    image = models.CharField(max_length=200)
    price = models.FloatField()
    total = models.FloatField()


Rating_Choices = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)


class Review(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey('Course.Course', related_name='reviews', on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(max_length=200, choices=Rating_Choices)

    def __str__(self):
        return str(self.course) + str(self.customer) + str(self.comment) + str(self.rating)
