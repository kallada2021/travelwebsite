import pytest 
from django.urls import reverse 

pytestmark = pytest.mark.django_db 

class TestSinglePages:
    def test_tour_single_url(self, client, tour_factory):
        tour = tour_factory()
        url = reverse("tour-single", kwargs={"tour": tour.name})
        response = client.get(url)
        assert response.status_code == 200 
        

    def test_destination_single_url(self, client, destination_factory):
        destination = destination_factory()
        url = reverse("destination-single", kwargs={"destination": destination.city})
        response = client.get(url)
        assert response.status_code == 200