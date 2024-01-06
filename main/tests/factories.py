import factory
from django.contrib.auth.models import User 
from main.models import Destination, Tour


class DestinationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Destination 
        
    city = "Hyderbad"
    country = "India"
    description = "It is an IT Hub also known as Hitech city"
    image = "images/destination/destination_1.jpg"


class TourFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tour
    
    name = "Hyderbad Tour"
    image = "images/tour/tour_1.jpg"
    description = "It is known for Golconda Fort, Charminar, and Biryani."
    price = 100
    duration = 3
    destination = factory.SubFactory(DestinationFactory)
