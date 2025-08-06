from django.urls import path

from . import views

urlpatterns = [
    path("list", views.PropertyList()),
    path("byId/<int:id>/", views.PropertyDetail()),
    path("createProperty/", views.PropertyCreate()),
    path("updateProperty/<int:id>/", views.PropertyUpdate()),
    path("deleteProperty/<int:id>/", views.PropertyDelete()),
]
