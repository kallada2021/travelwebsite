import factory,uuid
from django.contrib.auth.models import User
from usermanagement.models import UserProfile, Booking
from main.tests.factories import TourFactory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User 
        
    password = "test"
    username = "test"
    is_superuser = True 
    is_staff = True 


class UserProfileFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = UserProfile
    
    user = factory.SubFactory(UserFactory)
    bio = "Enthusiastic Traveller"
    location = "Hyderabad"
    phone_number = "1225-444-5555"

class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking
    
    booking_id = uuid.uuid4()
    is_paid = False
    traveller = factory.SubFactory(UserProfileFactory)
    tour = factory.SubFactory(TourFactory)
    