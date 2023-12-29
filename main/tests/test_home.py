import pytest 
from django.urls import reverse 
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db 

class TestHomePage:

    #TODO: Write a test class for the destination page and a test to test it returns a 200
    def test_homepage_url(self, client):
        url = reverse("homepage")
        response = client.get(url)
        assert response.status_code == 200
    
    def test_destinationpage_url(self, client):
        url = reverse("destinationpage")
        response = client.get(url)
        assert response.status_code == 200