from django.shortcuts import render

#TODO: Complete the register view by saving the user and creating a profile and rendering the registration page
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            #TODO: save in DB
            pass 
    
    return render(request, "registerpage goes here!!", context=context)
        