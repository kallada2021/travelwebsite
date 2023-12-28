from . import views
from django.urls import path

# TODO: add path for single views
urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("destinations/", views.DestinationView.as_view(), name="destinationpage"),
]
