from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login
from ecommerce.models import *
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            user.save()

            customer = Customer()
            customer.user = user
            customer.save()
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #Customer.objects.create(user=user, name=username, email= email) 
            messages.success(request, f'{username}, your account has been created! You are able to log in')
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')