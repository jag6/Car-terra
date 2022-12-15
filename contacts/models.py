from django.db import models
from datetime import datetime
from listings.models import Listing
from django.contrib.auth.models import User

class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    #listing = models.CharField(max_length=200)
    #listing_id - models.IntegerField()
    #user_id = models.IntegerField(blank=True)