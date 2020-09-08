from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ResumeDetails(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField()
    phone= models.IntegerField()
    address= models.TextField()
    college= models.TextField()
    skills= models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class Internships(models.Model):
    user=models.ForeignKey(ResumeDetails,on_delete=models.CASCADE)
    Organization_name=models.TextField()
    start=models.DateField()
    end=models.DateField()
    description=models.TextField()

class Projects(models.Model):
    user=models.ForeignKey(ResumeDetails,on_delete=models.CASCADE)
    project_name=models.TextField()
    project_description=models.TextField()
    url=models.URLField()
    image=models.ImageField()
