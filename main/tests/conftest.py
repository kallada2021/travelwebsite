from pytest_factoryboy import register 
from .factories import DestinationFactory, TourFactory

register(DestinationFactory)
register(TourFactory)