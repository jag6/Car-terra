from django.db import models
from datetime import datetime
from employees.models import Employee

class Listing(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    description = models.TextField(blank=True) 
    body_style = models.CharField(max_length=20, null=True)
    make = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=20, null=True)
    year = models.IntegerField(null=True)
    condition = models.CharField(max_length=20, null=True)
    price = models.IntegerField(null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title
    
    #blank=True = admin input optional
    #def __str__(self) = listing's main field