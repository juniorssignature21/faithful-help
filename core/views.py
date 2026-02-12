from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


from core.forms import CreateContactForm, BookAppointmentForm
from accounts.models import Profile

# Create your views here.
def error_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)
def error_500_view(request):
    return render(request, 'errors/500.html', status=500)
def error_403_view(request, exception):
    return render(request, 'errors/403.html', status=403)
def error_400_view(request, exception):
    return render(request, 'errors/400.html', status=400)

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

@login_required(login_url='accounts:login')
def book_appointment(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        messages.error(request, "Complete your profile")
        return redirect('accounts:create-profile')
    
    initial_data = {
        'full_name': profile.get_fullname(),
        'phone': profile.phone_number if hasattr(profile, 'phone_number') else '',
        'email': request.user.email,
    }
    
    form = BookAppointmentForm(initial=initial_data)
    
    if request.method == "POST":
        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, "Your appointment has been booked successfully!")
            return redirect("core:book-appointment")
        else:
            form_errors = {}
            
            for field, errors in form.errors.items():
                for error in errors:
                    form_errors[field] = error
            
            messages.error(request, f"{[f for f in form_errors.keys()]} : {[e for e in form_errors.values()]}")
        
        form = BookAppointmentForm(initial=initial_data)
    context = {
        'form':form
    }
            
    return render(request, "core/appointment.html", context)

def services(request):
    return render(request, "core/services.html")

@login_required(login_url='accounts:login')
def contact(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        messages.error(request, "Complete your profile")
        return redirect('accounts:create-profile')
    initial_data = {
        'full_name': profile.get_fullname(),
        'phone': profile.phone_number if hasattr(profile, 'phone_number') else '',
        'email': request.user.email,
    }
    form = CreateContactForm(initial=initial_data)
    
    if request.method == "POST":
        form = CreateContactForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            try:
                html_message = render_to_string("email_templates/contact.html", {
                    'full_name':form.cleaned_data['full_name'],
                    'email':form.cleaned_data['email'],
                    'phone':form.cleaned_data['phone'],
                    'subject': form.cleaned_data['subject'],
                    'message': form.cleaned_data['message']
                })
                
                send_mail(
                    subject=f"New Contact Message: {form.cleaned_data['subject']}",
                    message="You have received a new message from the contact form.",
                    from_email=form.cleaned_data['email'],
                    recipient_list=['chibuzor.john.2018@gmail.com'],  # Replace with your admin email
                    html_message=html_message
                )
                messages.success(request, "Your message has been sent successfully!")
                return redirect("core:contact")
            except Exception as e:
                messages.error(request, f"An error occurred while sending your message: {e}")
                return redirect("core:contact")
            
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect("core:contact")
    else:
        form = CreateContactForm(initial=initial_data)
    return render(request, "core/contact.html", {"form": form, "profile": profile})

def our_team(request):
    return render(request, "core/doctor.html")
