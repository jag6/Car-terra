from django.shortcuts import render
from listings.models import Listing
from employees.models import Employee
from listings.options import price_options, state_options

#index page
def index(request):
    search_states = Listing.objects.distinct('state')
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    listing_cont_title = 'Latest Listings'
    
    context = { 
                'search_states': search_states,
                'listings': listings,
                'price_options': price_options,
                'state_options': state_options,
                'listing_cont_title': listing_cont_title
                }
    
    return render(request, 'pages/index.html', context)

#about page
def about(request):
    employees = Employee.objects.order_by('hire_date')
    mvp_employees = Employee.objects.all().filter(is_mvp = True)
    
    context = { 
                'employees': employees,
                'mvp_employees': mvp_employees
                }
    
    return render(request, 'pages/about.html', context)