from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']