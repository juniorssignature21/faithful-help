from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import UserRegistrationForm

User = get_user_model()

# Create your views here.
def register_user(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Registration Successful!!")
            return redirect('core:home')
        else:
            messages.success(request, "There was a Problem Registring!!!")
            return redirect('accounts:register')
    
    form = UserRegistrationForm()
    
    context = {
        "form":form
    }
            
    return render(request, "register.html", context)

