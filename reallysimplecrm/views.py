from django.shortcuts import render

# Create your views here.

# Home page
def home(request):
    return render(request, 'home.html', {})
