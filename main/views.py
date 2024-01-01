from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Destination, Tour 

class HomeView(ListView):
    model = Tour 
    context_object_name = "tours"
    paginate_by = 10
    
    def get_template_names(self):
        # if self.request.htmx:
        #     return "components/post-list-elements.html"
        return "index.html"


#template for destinations page
class DestinationView(ListView):
    model = Destination
    context_object_name = "destinations"
    paginate_by = 10

    def get_template_names(self):
        return "destination.html"
    
  
def destination_single(request, destination):
    destination =get_object_or_404(Destination, city = destination)
    related = Destination.objects.filter(city=destination.city)[:5]
    return render(request, "single-destination.html", {"destination": destination, "related": related})
   
def tour_single(request, tour):
    tour = get_object_or_404(Tour,name=tour)
    related = Tour.objects.filter(name=tour.name)[:5]
    return render(request, "single-tour.html", {"tour": tour, "related": related})

    