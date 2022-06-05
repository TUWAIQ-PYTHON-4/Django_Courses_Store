from django.db import models
from django.contrib.auth.models import User

class Cuorse(models.Model):
    title= models.CharField(max_length=200)
    desc = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    online = models.BooleanField()
    stert_data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Review (models.Model):
    course = models.ForeignKey(Cuorse , on_delete=models.DO_NOTHING)
    rating = models.IntegerField(max_length=10)
    comment = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    def __str__(self):
        return self.course


class Order (models.Model):
    course =models.ForeignKey(Cuorse , on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    totalprice = models.DecimalField(max_digits=10 , decimal_places=2)
    def __str__(self):
        return str(self.course)