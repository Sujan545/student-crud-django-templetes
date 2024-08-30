from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1,blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
   # image= models.ImageField(upload_to=settings.MEDIA_ROOT)
    faculty_choices = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA')
    )
    faculty=models.CharField(max_length=10,choices = faculty_choices,default='BCA')

    def __str__(self):
        return self.name
