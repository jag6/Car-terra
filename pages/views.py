from django.shortcuts import render
from listings.models import Listing
from employees.models import Employee

def index(request):
    search_listings = Listing.objects.all().distinct('state')
    newest_listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    
    context = { 
                'search_listings': search_listings,
                'newest_listings': newest_listings 
                }
    
    return render(request, 'pages/index.html', context)

def about(request):
    employees = Employee.objects.order_by('hire_date')
    mvp_employees = Employee.objects.all().filter(is_mvp = True)
    
    context = { 
                'employees': employees,
                'mvp_employees': mvp_employees
                }
    
    return render(request, 'pages/about.html', context)