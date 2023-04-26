from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here. (Backend so to speak)

# Notes
# request = someone going into a web page and requesting to do something like login or logout
# login and logout are functions that's why we must use def login_user and def logout_user


# Home page
def home(request):
    # Check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(
                request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')


    else:
        return render(request, 'home.html', {})

# Login/Logout User
# def login_user(request):
#     pass


def logout_user(request):
    pass
