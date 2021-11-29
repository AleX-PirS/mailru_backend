from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

from .views import CitiesViewSet, PicturesViewSet, LocationsViewSet


router_city = DefaultRouter()
router_city.register(r'api/cities', CitiesViewSet, basename='cities')

router_picture = DefaultRouter()
router_picture.register(r'api/pictures', PicturesViewSet, basename='pictures')

router_location = DefaultRouter()
router_picture.register(r'api/locations', LocationsViewSet, basename='locations')

routers = [router_city, router_picture, router_location]

urlpatterns = [
]

for single_router in routers:
    urlpatterns += single_router.urls
