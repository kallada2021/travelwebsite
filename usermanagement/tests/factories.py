import factory
from django.contrib.auth.models import User 

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User 
        
    password = "test"
    username = "test"
    is_superuser = True 
    is_staff = True 


# TODO: Create UserProfile Factory and register the factories on conftest.py