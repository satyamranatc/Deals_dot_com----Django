from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("api/city/", include("City.urls")),
    path("api/property/", include("Property.urls")),
    path("admin/", admin.site.urls),
]
