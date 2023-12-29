from pytest_factoryboy import register 
from .factories import DestinationFactory, TourFactory

# TODO: register Tour Factory
register(DestinationFactory)
register(TourFactory)