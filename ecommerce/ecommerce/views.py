from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse('Home page')

def about(request):
    return HttpResponse('About page')

def profile(request):
    return HttpResponse('Profile page')

def gallery(request):
    return HttpResponse('Gallery page')