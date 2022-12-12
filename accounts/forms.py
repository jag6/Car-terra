from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, label='first_name'),
    last_name = forms.CharField(max_length=20, label='last_name'),
    username = forms.CharField(max_length=20, label='username'),
    email = forms.EmailField(max_length=30, label='email'),
    password = forms.CharField(max_length=20, label='password')
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        )
    
    #validate form data
    def clean(self):
        super(RegisterForm, self).clean()

        #validate first name        
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            self.add_error('first_name', 'Please fill in first name')
        elif len(first_name) <= 1:
            self.add_error('first_name', 'First name must be at least 2 characters long')
        
        #validate last name
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            self.add_error('last_name', 'Please fill in last name')
        elif len(last_name) <= 1:
            self.add_error('last_name', 'Last name must be at least 2 characters long')
            
        #validate username
        username = self.cleaned_data.get('username')
        if not username:
            self.add_error('username', 'Please fill in username')
        elif len(username) <= 3:
            self.add_error('username', 'Username must be at least 4 characters long')
        elif User.objects.filter(username = username).exists():
            self.add_error('username', 'Username is taken')
    
        #validate email
        email = self.cleaned_data.get('email')
        if not email:
            self.add_error('email', 'PLease fill in email')
        elif User.objects.filter(email = email).exists():
            self.add_error('email', 'Email already in use')
    
        #validate password
        password = self.cleaned_data.get('password')
        if not password:
            self.add_error('password', 'Please fill in password')
        elif len(password) <= 7:
            self.add_error('password', 'Password must be at least 8 characters long')
            
        return self.cleaned_data