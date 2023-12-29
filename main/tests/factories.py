import factory
from django.contrib.auth.models import User 
from main.models import Destination

class DestinationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Destination 
        
    city = "Hyderbad"
    country = "India"
    #TODO: create factory fields for the remaining Model fields
    

# TODO: Create a Factory for the Tour model