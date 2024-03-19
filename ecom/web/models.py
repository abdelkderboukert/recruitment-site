from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class user(models.Model):
    first_name = models.CharField(max_length=20, unique=False)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class condition(models.Model):
    age = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.age}"

class job(models.Model):
    name = models.CharField(max_length=50, unique=True)
    details = models.TextField()
    salary = models.IntegerField()
    hour = models.IntegerField(default=8)
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/info/')
    condition = models.OneToOneField(condition, on_delete=models.CASCADE)
    user = models.ManyToManyField('info')

    def __str__(self):
        return f"{self.name} {self.details}"

class info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobs = models.ManyToManyField('job')
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.last_name