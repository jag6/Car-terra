from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from listings.models import Listing
from . forms import InquiryForm
from . models import Inquiry

def inquiry(request):
    form = InquiryForm(request.POST, Listing, User)
    
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        
        if form.is_valid():
            #sanitize form
            inquiry=Inquiry(listing = Listing.objects.get(title=form.cleaned_data['listing']), name=form.cleaned_data['name'], email=form.cleaned_data['email'], phone=form.cleaned_data['phone'], message=form.cleaned_data['message'], user = User.objects.get(username=form.cleaned_data['user']))
            #save inquiry
            inquiry.save()
            #success message and redirect
            messages.success(request, 'Thank you for your inquiry. A representative will be in contact with you shortly.')
            return redirect('/listings/' + listing_id)