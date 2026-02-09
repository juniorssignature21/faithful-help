from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def book_appointment(request):
    return render(request, "appointment.html")