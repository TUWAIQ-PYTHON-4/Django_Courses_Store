from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=70)
    desc=models.TextField()
    duration=models.IntegerField()
    price=models.FloatField()
    image=models.ImageField(upload_to='images/')
    online=models.BooleanField()
    start_date=models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    rating=models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])
    comment=models.TextField() 
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date=models.DateField(auto_now_add= True)
    totalprice=models.FloatField()



    

