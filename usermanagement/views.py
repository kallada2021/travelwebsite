from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth 
from .forms import CreateUserForm, LoginForm, BookingForm
from .models import UserProfile, Booking
from main.models import Tour

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
            return redirect("login")

    context = {"form":form}
    return render(request, "usermanagement/register.html", context=context)
    
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
                return redirect("homepage")
            
    context = {"form": form}
    return render(request, "usermanagement/login.html", context=context)

def user_logout(request):
    auth.logout(request)
    return redirect("None")


def booking(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            traveller_id = request.POST.get("traveller")
            user_profile = UserProfile.objects.get(pk = traveller_id)
            tour = request.POST.get("tour")
            tour_id = Tour.objects.get(pk = tour)
            booking = Booking.objects.create(traveller = user_profile, tour = tour_id)
            booking.save()
            return redirect("homepage")
    context = {"form": form}
    return render(request, "bookings.html", context=context)

