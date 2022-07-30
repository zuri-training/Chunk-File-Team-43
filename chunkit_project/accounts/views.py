from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def registerPage(request):
    context = {}
    return render(request, 'accounts/sign-up.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def forgotPassword(request):
    context = {}
    return render(request, 'accounts/reset-password.html', context)

def setPassword(request):
    context = {}
    return render(request, 'accounts/set-new-password.html', context)
