from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cities, Pictures, Locations
from .serializers import CitiesSerializer, PicturesSerializer, LocationsSerializer


def index(request):
    name = request.GET.get('name')
    if name is None:
        name = 'Anon'
    ctx = {'name': name}
    return render(request, 'index.html', ctx)


class CitiesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Cities.objects.all()
        serializer = CitiesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cities.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        serializer = CitiesSerializer(city)
        return Response(serializer.data)

    def create(self, request):
        serializer = CitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Cities.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        serializer = CitiesSerializer(instance=city, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Cities.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        serializer = CitiesSerializer(city)
        city.delete()
        return Response(serializer.data)


class PicturesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Pictures.objects.all()
        serializer = PicturesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Pictures.objects.all()
        picture = get_object_or_404(queryset, pk=pk)
        serializer = PicturesSerializer(picture)
        return Response(serializer.data)

    def create(self, request):
        serializer = PicturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Pictures.objects.all()
        picture = get_object_or_404(queryset, pk=pk)
        serializer = PicturesSerializer(instance=picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Pictures.objects.all()
        picture = get_object_or_404(queryset, pk=pk)
        serializer = PicturesSerializer(picture)
        picture.delete()
        return Response(serializer.data)


class LocationsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Locations.objects.all()
        serializer = LocationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Locations.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationsSerializer(location)
        return Response(serializer.data)

    def create(self, request):
        serializer = LocationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Locations.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationsSerializer(instance=location, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Locations.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationsSerializer(location)
        location.delete()
        return Response(serializer.data)
