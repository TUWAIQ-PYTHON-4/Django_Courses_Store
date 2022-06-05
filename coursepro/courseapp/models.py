from django.db import models
from django.contrib.auth.models import User

class course(models.Model):
    title=models.CharField(max_length=50)
    duration=models.IntegerField()
    start_date=models.DateField()
    price=models.FloatField()
    description=models.TextField(max_length=240)
    image= models.ImageField(upload_to="images/")
    online=models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return '{} {} {}'.format(self.user, self.title, self.price)

class Review(models.Model):
    rating=models.IntegerField(max_length=5 ,help_text='The rating into 5')
    comment=models.TextField(max_length=240)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    namecourse =models.ForeignKey(course, on_delete=models.CASCADE , related_name='Reviews')


class order(models.Model):
    course=models.CharField(max_length=50)
    date=models.DateField()
    totalprice=models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user+" "+self.course+ " " +self.totalprice+" "+self.date
