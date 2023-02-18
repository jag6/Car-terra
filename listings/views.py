from django.shortcuts import render, get_object_or_404
from . models import Listing
from . options import price_options, state_options

#listings page
def index(request):
    #listings info
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    listing_cont_title = 'All Listings'
    
    #head tags
    title = 'Listings'
    description = 'Listings page'
    image = 'listings-banner.webp'
    url = '/listings'
    
    #banner
    banner_title = 'BROWSE OUR LISTINGS'
    banner_img = 'listings-banner.webp'
    banner_img_description = 'Chevy Camaro'
    
    context = { 
                'listings': listings,
                'listing_cont_title': listing_cont_title,
                'title': title,
                'description': description,
                'image': image,
                'url': url,
                'banner_title': banner_title,
                'banner_img': banner_img,
                'banner_img_description': banner_img_description
                }
    
    return render(request, 'listings/listings.html', context)

#listing page
def listing(request, listing_id):
    #listing info
    listing = get_object_or_404(Listing, pk = listing_id)
    
    #similar listings info
    similar_listings = Listing.objects.filter(is_published = True)
    
    #head tag
    url = '/listing/'
    
    context = { 
                'listing': listing,
                'similar_listings': similar_listings,
                'url': url
                }
    
    return render(request, 'listings/listing.html', context)

#search page
def search(request):
    #search info
    queryset_list = Listing.objects.order_by('-price', '-list_date')
    search_states = Listing.objects.distinct('state')
    listing_cont_title = 'Your Results'
    
    #head tags
    title = 'Search'
    description = 'Search page'
    image = 'search-banner.webp'
    url = '/search'
    
    #keyword
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            queryset_list = queryset_list.filter(description__icontains = keyword)
    
    #make
    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            queryset_list = queryset_list.filter(make__iexact = make)
    
    #model
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            queryset_list = queryset_list.filter(model__icontains = model)
            
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)
            
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)
    
    
    context = { 
                'listings': queryset_list,
                'search_states': search_states,
                'values': request.GET,
                'listing_cont_title': listing_cont_title,
                'price_options': price_options,
                'state_options': state_options,
                'title': title,
                'description': description,
                'image': image,
                'url': url
                }
    
    return render(request, 'listings/search.html', context)