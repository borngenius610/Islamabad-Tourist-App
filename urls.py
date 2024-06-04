from django.contrib import admin
from django.urls import path
from playground import views

urlpatterns = [
   path("", views.index, name= 'home' ),
   path("about", views.about, name= 'about' ),
   path("faqs", views.faqs, name= 'faqs' ),
   path("hotel", views.hotel, name= 'hotel' ),
   path("tour", views.tour, name= 'tour' ),
   path("car", views.car, name= 'car' ),
]
