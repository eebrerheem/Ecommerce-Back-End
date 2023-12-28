from django.shortcuts import render
from database.models import Product

# Create your views here.

def home(request):
    
    return render(request, 'home.html')
