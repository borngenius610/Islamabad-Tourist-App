from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def hotel(request):
    return render(request, 'hotel.html')

def tour(request):
    return render(request, 'tour.html')

def car(request):
    return render(request, 'car.html')