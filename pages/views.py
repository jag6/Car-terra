from django.shortcuts import render
from listings.models import Listing
from employees.models import Employee
from listings.options import price_options, state_options

#index page
def index(request):
    search_states = Listing.objects.distinct('state')
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    listing_cont_title = 'Latest Listings'
    
    title = 'Home'
    description = 'Homepage'
    image = '/static/images/car-banner.jpg'
    
    context = { 
                'search_states': search_states,
                'listings': listings,
                'price_options': price_options,
                'state_options': state_options,
                'listing_cont_title': listing_cont_title,
                'title': title,
                'description': description,
                'image': image,
                }
    
    return render(request, 'pages/index.html', context)

#about page
def about(request):
    employees = Employee.objects.order_by('hire_date')
    mvp_employees = Employee.objects.all().filter(is_mvp = True)
    
    title = 'About'
    description = 'About page'
    image = '/static/images/about-banner.jpg'
    url = '/about'
    
    context = { 
                'employees': employees,
                'mvp_employees': mvp_employees,
                'title': title,
                'description': description,
                'image': image,
                'url': url
                }
    
    return render(request, 'pages/about.html', context)