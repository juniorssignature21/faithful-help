from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


from core.forms import CreateContactForm
from accounts.models import Profile

# Create your views here.
def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def book_appointment(request):
    return render(request, "core/appointment.html")

def services(request):
    return render(request, "core/services.html")

@login_required(login_url='accounts:login')
def contact(request):
    form = CreateContactForm()
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = CreateContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
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

    return render(request, "core/contact.html", {"form": form, "profile": profile})