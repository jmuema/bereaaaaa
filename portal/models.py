from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=200)
    class_id = models.CharField(max_length=20)
    
    def __str__(self):
        return self.class_name





class Unit(models.Model):
    unit_name = models.CharField(max_length= 60)
    unit_code = models.CharField(max_length=60)
    tutor_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby', on_delete=models.CASCADE)
    tutor_contact = models.CharField(max_length=10)
    classroom_id = models.ManyToManyField(Classroom)


    def __str__(self):
        return self.unit_name

class Notes(models.Model):
    note = models.FileField(null = True, upload_to='notes')
    unit = models.ForeignKey(Unit, on_delete= models.CASCADE, null = True)  
    note_title = models.CharField(null=True,max_length=30)
    def __str__(self):
        return self.note_title

class Task(models.Model):
    assignment_name = models.CharField(max_length = 60)
    assignment = models.FileField(null = False, upload_to='assignments')
    unit_id = models.ForeignKey(Unit, on_delete= models.CASCADE, null = True)


	
