from pytest_factoryboy import register 
from .factories import UserFactory,UserProfileFactory,BookingFactory

register(UserFactory)
register(UserProfileFactory)
register(BookingFactory)