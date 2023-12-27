from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("", views.DestinationView.as_view(), name="destinationpage"),
]
