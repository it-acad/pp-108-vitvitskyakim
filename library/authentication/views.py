from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser
from django.contrib import messages


def home(request):
    return render(request, 'authentication/home.html')
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        middle_name = request.POST.get("middle_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        role = request.POST.get("role")
        if role == "user":
            role = 0
        elif role == "librarian":
            role = 1
        else:
            role = 0 

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'authentication/register.html')

        user = CustomUser.create(first_name=first_name, last_name=last_name, middle_name=middle_name, 
                                 email=email, password=password1, role=role)
        if user:
            return redirect('/') 
        messages.error(request, 'Registration failed. Please try again.')
        return render(request, 'authentication/register.html')
    
    return render(request, 'authentication/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Try again!")
            return render(request, 'authentication/login.html')
    return render(request, 'authentication/login.html')
def logout(request):
    auth_logout(request)
    return redirect("/")



def is_librarian(user):
    return user.role == 1

@user_passes_test(is_librarian)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'authentication/user_list.html', {'users': users})

@user_passes_test(is_librarian)
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'authentication/user_detail.html', {'user': user})