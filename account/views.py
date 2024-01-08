from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        data = RegistrationForm(request.POST)
    
    return render(request, 'account/registration.html', {'form': form})

