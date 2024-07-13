from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse

from authentication.models import User
from django.contrib.auth import authenticate,login as auth_login

# Create your views here.
def home(request):
    return render(request, 'authentication/home.html')

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
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:    
            messages.success(request, 'Login successful')
            # auth_login(request, user) #
            # fname = user.first_name
            return redirect('home')  # Redirect to home after successful login
        
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        
    else:
        return render(request, 'authentication/login.html')

def logout(request):
    pass # pass is a placeholder that does nothing