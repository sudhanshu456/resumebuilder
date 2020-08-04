from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ResumeDetails(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    phone= models.IntegerField()
    address= models.TextField()
    college= models.TextField()
    skills= models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


    