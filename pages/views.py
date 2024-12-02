from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return HttpResponse("Welcome to the pages home page!")

def about(request):
    return render(request, 'pages/about.html')  
def contact(request):
    return render(request, 'contact.html')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_warning(request):
    return render(request, 'pages/logout_warning.html')

def confirm_logout(request):
    return redirect('logout')

def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    return render(request, 'registration/sign_up.html', {'form': form})