from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from listings.models import Listing
from . forms import InquiryForm
from . models import Inquiry

def inquiry(request):
    form = InquiryForm(request.POST, Listing, User)
    
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        
        if form.is_valid():
            listing = Listing.objects.get(title=form.cleaned_data['listing'])
            user = User.objects.get(username=form.cleaned_data['user'])
            listing_title = request.POST['listing_title']
            employee_email = request.POST['employee_email']
            
            #check for previous inquiry
            if request.user.is_authenticated:
                has_contacted = Inquiry.objects.all().filter(listing = listing, user = user)
                if has_contacted:
                    messages.error(request, 'You\'ve already made an inquiry for this listing')
                    return redirect('/listings/' + listing_id)
                
            #sanitize form
            inquiry=Inquiry(listing = listing, name=form.cleaned_data['name'], email=form.cleaned_data['email'], phone=form.cleaned_data['phone'], message=form.cleaned_data['message'], user = user)
            
            #save inquiry
            inquiry.save()
            
            #send email
            send_mail(
                'Car-terra Listing Inquiry',
                'Inquiry for ' + listing_title + '. Sign into the admin panel for more info',
                EMAIL_HOST_USER,
                [employee_email],
                fail_silently=False
            )
            
            #success message and redirect
            messages.success(request, 'Thank you for your inquiry. A representative will be in contact with you shortly.')
            return redirect('/listings/' + listing_id)
        else:
            messages.error(request, 'Please enter your phone number')
            return redirect('/listings/' + listing_id)