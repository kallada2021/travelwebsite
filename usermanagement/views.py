from django.shortcuts import render
from .forms import CreateUserForm
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

    context = {"form":form}
    return render(request, "usermanagement/register.html", context=context)
    
#TODO: Add a login view and a logout view