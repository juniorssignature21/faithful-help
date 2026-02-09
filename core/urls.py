from django.urls import path
from .views import home, about, book_appointment

app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('book-appointment/', book_appointment, name='book-appointment'),
]
