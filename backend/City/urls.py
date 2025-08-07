from django.urls import path

from . import views

urlpatterns = [
    path("list", views.CityList),
    path("byId/<int:id>/", views.CityDetail),
    path("createCity/", views.CityCreate),
    path("updateCity/<int:id>/", views.CityUpdate),
    path("deleteCity/<int:id>/", views.CityDelete),

]
