from rest_framework import generics
from .serializers import CitiesSerializer
from .models import Cities


class CitiesCreateApi(generics.CreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer