from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse

from authentication.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.hashers import check_password


# Create your views here.
def home(request):
    return render(request, 'authentication/home.html')

def todoIndex(request):
    return render(request, 'todo/index.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']

        myuser= User.objects.create(firstname=firstname, lastname=lastname, address=address, email=email, password=password)
        myuser.save()
        messages.success(request, 'User created successfully')
        return redirect('login')
    else:
        messages.error(request, 'User not created')
        return render(request, 'authentication/signup.html')
    

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('todoIndex')  # Redirect to home after successful login
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        
    return render(request, 'authentication/login.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('login')