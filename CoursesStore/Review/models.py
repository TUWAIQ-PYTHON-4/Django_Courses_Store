from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Review :
# rating
# comment
# user (use the User from Django auth models)

# Rating_Choices = (
#     ('5', '5'),
#     ('4', '4'),
#     ('3', '3'),
#     ('2', '2'),
#     ('1', '1'),
# )
#
#
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     course = models.ForeignKey('Course.Course', on_delete=models.DO_NOTHING)
#     comment = models.TextField()# #     rating = models.CharField(max_length=200, choices=Rating_Choices)
# #
# #     def __str__(self):
# #         return self.course
