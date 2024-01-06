from pytest_factoryboy import register 
from .factories import UserFactory,UserProfileFactory

register(UserFactory)
register(UserProfileFactory)