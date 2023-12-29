import pytest 

pytestmark = pytest.mark.django_db

class TestDestinationModel:
    def test_str_return(self, destination_factory):
        dest = destination_factory(city="Hyderbad")
        assert dest.__str__() == f"{dest}"
        
# Write a test case for the Tour Model str method

class TestTourModel:
    def test_str_return(self, tour_factory):
        tour = tour_factory(name="Hyderabad Tour")
        assert tour.__str__() == f"{tour}"