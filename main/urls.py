from . import views
from django.urls import path


# TODO: Add url for tags
urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("tour/<str:tour>", views.tour_single, name = "tour-single"),
    path("destinations/", views.DestinationView.as_view(), name="destination-page"),
    path("destinations/<str:destination>", views.destination_single, name = "destination-single"),
    path("tag/<slug:tag>/", views.TagListView.as_view(), name="post-by-tag"),
]
