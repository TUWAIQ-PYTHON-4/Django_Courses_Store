from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    course = models.ManyToManyField('Course.Course', blank=True)

    def __str__(self):
        return str(self.user)



