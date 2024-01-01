from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("tour/<str:tour>", views.tour_single, name = "tour-single"),
    path("destinations/", views.DestinationView.as_view(), name="destinationpage"),
    path("destinations/<str:destination>", views.destination_single, name = "destination-single"),
]
