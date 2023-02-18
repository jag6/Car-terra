from django.db import models
from django.conf import settings
from datetime import datetime
from listings.models import Listing

class Inquiry(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True)
    inquiry_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name