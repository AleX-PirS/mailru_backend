from django.urls import path
from mymaps import views

urlpatterns = [
    path('', views.map_detail, name='map_detail'),
    path('map_create/', views.map_create, name='map_create'),
    path('map_list/', views.map_list, name='map_list'),
]
