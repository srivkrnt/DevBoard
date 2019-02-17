from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

def dashboard(request):
    return render(request, 'forum/dashboard.html')
def index(request):
    return render(request, 'forum/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('dashboard')

    else:
        form = UserRegistrationForm()
    return render(request, 'forum/register.html', {'form':form})
