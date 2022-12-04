from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'employee')
    list_display_links = ('id', 'title')
    list_filter = ('employee', 'make')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'body_style', 'make', 'model', 'year', 'color', 'condition', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)