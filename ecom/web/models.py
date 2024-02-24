from django.db import models
import datetime
from django.utils import timezone

class user(models.Model):
    first_name = models.CharField(max_length=20, unique=False)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class info(models.Model):
    use = models.ForeignKey(user, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=2)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/info/')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.last_name