from django.contrib import admin

from .models import Cities, Locations, Pictures


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Locations)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city', )
    search_fields = ('name', )


@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'author')
    list_filter = ('author', 'location')
    search_fields = ('name', )
