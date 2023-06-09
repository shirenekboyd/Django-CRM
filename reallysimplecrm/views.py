from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, NewContactForm
from .models import Contact
from django.utils import timezone

# Create your views here. (Backend so to speak)

# Notes
# request = someone going into a web page and requesting to do something like login or logout
# login and logout are functions that's why we must use def login_user and def logout_user


# Home & Login page
def home(request):
    # grab everything in Contact table and assign it to this variable
    contacts = Contact.objects.all()

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
        return render(request, 'home.html', {'contacts':contacts})

# Logout User
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

# Register User
def register_user(request): 
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
        # else user hasn't filled out the form and needs to be presented with the form
    else: 
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})  
        
# CRUD Operations below
# @login_required
def contact_detail(request, pk):
    if request.user.is_authenticated:
        # Look Up a single Contact from Contacts
        customer_contact = Contact.objects.get(id=pk)
        return render(request, 'contact_detail.html', {'customer_contact':customer_contact})
    # if user is not authenticated
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

# @login_required
def contact_delete(request, pk):
    if request.user.is_authenticated:
        delete_it = Contact.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Contact Deleted Successfully!")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Delete A Contact...")
        return redirect('home')

# @login_required
def contact_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewContactForm(request.POST, request.FILES)
            if form.is_valid():
                new_contact = form.save(commit=False)
                new_contact.user = request.user
                new_contact.save()
                messages.success(request, "New Contact Added...")
                return redirect('home')
        else:
            form = NewContactForm()
        return render(request, 'contact_create.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In To Create A New Contact...")
        return redirect('home')
    
# @login_required
def contact_update(request, pk):
    if request.user.is_authenticated:
        current_contact = Contact.objects.get(id=pk)
        if request.method == "POST":
            form = NewContactForm(request.POST, request.FILES, instance=current_contact)
            if form.is_valid():
                updated_contact = form.save(commit=False)
                updated_contact.updated_at = timezone.now()  # Set the updated_at field with the current time
                if 'profile_picture-clear' in request.POST and request.POST['profile_picture-clear'] == 'on':
                    updated_contact.profile_picture = 'profile_pictures/default.png'
                elif request.FILES.get('profile_picture'):
                    updated_contact.profile_picture = request.FILES['profile_picture']
                updated_contact.save()
                messages.success(request, "Contact Has Been Updated!")
                return redirect('home')
        else:
            form = NewContactForm(instance=current_contact)
        return render(request, 'contact_update.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In To Edit A Contact...")
        return redirect('home')






        






