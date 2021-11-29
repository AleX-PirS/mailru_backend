from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *

User = get_user_model()


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

    def validate_lt(self, value):
        if value < -90.0 or value > 90.0:
            raise serializers.ValidationError('Wrong range to latitude [-90.0:90.0]')
        return value

    def validate_lg(self, value):
        if value < 0.0 or value > 180.0:
            raise serializers.ValidationError('Wrong range to longitude [0.0:180.0]')
        return value


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'

    def validate_lt(self, value):
        if value < -90.0 or value > 90.0:
            raise serializers.ValidationError('Wrong range to latitude [-90.0:90.0]')
        return value

    def validate_lg(self, value):
        if value < 0.0 or value > 180.0:
            raise serializers.ValidationError('Wrong range to longitude [0.0:180.0]')
        return value


class PicturesSerializer(serializers.ModelSerializer):
    location = serializers.CharField(read_only=True)
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Pictures
        fields = '__all__'
