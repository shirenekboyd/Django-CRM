from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# Create your views here.

# Notes
# request = someone going into a web page and requesting to do something like login or logout
# login and logout are functions that's why we must use def login_user and def logout_user



# Home page
def home(request):
    return render(request, 'home.html', {})

# Login/Logout User 
# def login_user(request):
#     pass

def logout_user(request):
    pass 