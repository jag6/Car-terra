from django.db import models
from datetime import datetime

class Employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    is_mvp = models.BooleanField(default=False, null=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name