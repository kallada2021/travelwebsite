import factory
from django.contrib.auth.models import User
from usermanagement.models import UserProfile

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