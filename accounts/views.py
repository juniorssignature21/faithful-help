from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, ProfileForm
from accounts.models import Profile

User = get_user_model()

# Create your views here.
def register_user(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)            
                messages.success(request, "Registration and Login Successful!!")
                return redirect('accounts:create-profile')
        else:
            
            for field, errors in form.errors.items():
               for error in errors:
                   messages.error(request, f"{field}: {error}")

            return redirect('accounts:register')
    
    form = UserRegistrationForm()
    
    context = {
        "form":form
    }
            
    return render(request, "accounts/register.html", context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            next_url = request.GET.get("next")
            return redirect(next_url) if next_url else redirect("core:home")
        else:
            messages.error(request, "Invalid email or password")
            return redirect("accounts:login")
    return render(request, "accounts/login.html")

def logout_user(request):
    logout(request)
    messages.info(request, "")
    path = request.META.get('HTTP_REFERER', '/')
    return redirect(path)

def create_profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile created successfully!")
            return redirect("core:home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect("accounts:create_profile")
    form = ProfileForm()
    context = {
        "form": form
    }
    return render(request, "accounts/create_profile.html", context)


@login_required(login_url='accounts:login')
def edit_profile(request):
    user = request.user
    profile =  Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("core:home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect("accounts:edit_profile")
    form = ProfileForm(instance=profile)
    context = {
        "form": form
    }
    return render(request, "accounts/edit_profile.html", context)


@login_required(login_url='accounts:login')
def view_profile(request):
    user = request.user
    profile =  Profile.objects.get(user=user)
    context = {
        "profile": profile
    }
    
    return render(request, "accounts/profile.html", context)