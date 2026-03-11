from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout

# Create your views here.
#homepage
def home(request):
    return render(request, 'users/home.html')
# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # create profile for additional fields
            Profile.objects.create(user=user, location=request.POST.get('location', ''))
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#login and logout views
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('register')  # or your homepage
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login') 
        
