import pytest 
from django.urls import reverse 

pytestmark = pytest.mark.django_db 

class TestTourSingle:
    def test_post_single_url(self, client, tour_factory):
        tour = tour_factory()
        url = reverse("tour-single", kwargs={"tour": tour.name})
        response = client.get(url)
        assert response.status_code == 200 
        
# TODO: Write a test to test the destination single page