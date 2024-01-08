from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout, authenticate

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        data = RegistrationForm(request.POST)
    else:
        form = RegistrationForm()
    
    return render(request, 'account/signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'account/signin.html')

def signout(request):
    logout(request)
    return redirect('index')
