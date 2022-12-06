from django.shortcuts import render, get_object_or_404
from . models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    
    context = { 'listings': listings }
    
    return render(request, 'listings/listings.html', context)
    
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    similar_listings = Listing.objects.filter(is_published = True)
    
    context = { 
                'listing': listing,
                'similar_listings': similar_listings
               }
    
    return render(request, 'listings/listing.html', context)
    
def search(request):
    return render(request, 'listings/search.html')