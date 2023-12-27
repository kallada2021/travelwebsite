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


class DestinationView(ListView):
    model = Destination
    context_object_name = "Destinations"
    paginate_by = 10
    