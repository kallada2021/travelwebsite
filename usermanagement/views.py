from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm, LoginForm
from .models import UserProfile

#Register view by saving the user and creating a profile and rendering the registration page
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            #save in DB
            current_user = form.save(commit=False)
            form.save()

            profile = UserProfile.objects.create(user=current_user)
            profile.save()
            return redirect("usermanagement/login.html")

    context = {"form":form}
    return render(request, "usermanagement/register.html", context=context)
    
#TODO: Add a login view and a logout view
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("index.html")
            
    context = {"form": form}
    return render(request, "usermanagement/login.html", context=context)

def user_logout(request):
    auth.logout(request)
    return redirect("None")