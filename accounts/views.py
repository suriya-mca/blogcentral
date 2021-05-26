from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# message module 
from django.contrib import messages

# Create your views here.

# register page
def regform(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
                
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User name taken')
                return redirect('regform')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('regform')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password and Confirm password not matching')
            return redirect('regform')
    else:
        return render(request, 'forms/register.html')

# login page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in Successfully.....')
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
         return render(request, 'forms/login.html')

# logout page
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out.....')
    return redirect('home')

