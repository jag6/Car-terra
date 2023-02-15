from django.shortcuts import render
from listings.models import Listing
from employees.models import Employee
from listings.options import price_options, state_options

#index page
def index(request):
    #listings info
    search_states = Listing.objects.distinct('state')
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    listing_cont_title = 'Latest Listings'
    
    #head tags
    title = 'Home'
    description = 'Looking for a quality pre-owned vehicle? Then you\'ve come to the right place, because we at Car-terra make customer satisfaction our #1 priority.'
    image = 'car-banner.webp'
    
    #banner
    banner_img = 'car-banner.webp'
    
    context = { 
                'search_states': search_states,
                'listings': listings,
                'price_options': price_options,
                'state_options': state_options,
                'listing_cont_title': listing_cont_title,
                'title': title,
                'description': description,
                'image': image,
                'banner_img': banner_img
                }
    
    return render(request, 'pages/index.html', context)

#about page
def about(request):
    #employee info
    employees = Employee.objects.order_by('hire_date')
    mvp_employees = Employee.objects.all().filter(is_mvp = True)
    
    #head tags
    title = 'About'
    description = 'Meet the dream team behind your favorite car listings company.'
    image = 'about-banner.webp'
    url = '/about'
    
    #banner
    banner_title = 'MEET THE DREAM TEAM'
    banner_img = 'about-banner.webp'
    banner_img_description = 'Car-terra sales team'
    
    context = { 
                'employees': employees,
                'mvp_employees': mvp_employees,
                'title': title,
                'description': description,
                'image': image,
                'url': url,
                'banner_title': banner_title,
                'banner_img': banner_img,
                'banner_img_description': banner_img_description
                }
    
    return render(request, 'pages/about.html', context)

#contact page
def contact(request):
    #head tags
    title = 'Contact'
    description = 'Feel free to contact us at any time. We eagerly await the opportunity to help you find the car of your dreams.'
    image = 'contact-banner.webp'
    url = '/contact'
    
    #banner
    banner_title = 'DROP US A LINE'
    banner_img = 'contact-banner.webp'
    banner_img_description = 'woman sending a text message'
    
    context = {
                'title': title,
                'description': description,
                'image': image,
                'url': url,
                'banner_title': banner_title,
                'banner_img': banner_img,
                'banner_img_description': banner_img_description
                }
    
    return render(request, 'pages/contact.html', context)