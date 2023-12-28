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


#TODO: Add template for destinations page
class DestinationView(ListView):
    model = Destination
    context_object_name = "Destinations"
    paginate_by = 10
    
 
# TODO: make a function view for single destinations   
   
def tour_single(request, tour):
    tour = get_object_or_404(Tour,city=tour)
    related = Tour.objects.filter(title=tour.city)[:5]
    return render(request, "single-tour.html", {"tour": tour, "related": related})

    