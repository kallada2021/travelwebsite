import pytest 
from django.urls import reverse 
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db 

class TestHomePage:
    #TODO: Write a test using the url client to check of the homepage url returns a 200
    #TODO: Write a test class for the destination page and a test to test it returns a 200
    def test_homepage_url(self, client):
        pass 