from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_detail, name='map_detail'),
    path('map_create/', views.map_create, name='map_create'),
    path('map_list/', views.map_list, name='map_list'),

    path('<slug:name>/<int:lt>/<int:lg>/create/',
         views.create, name='create_city'),
    path('<int:city_id>/detail/', views.detail, name='detail'),
    path('all_cities/', views.all_cities, name='all_cities'),
    path('<int:city_id>/<slug:new_name>/change_name/',
         views.change_name, name='change_name'),
    path('<int:city_id>/delete_city/', views.delete_city, name='delete_city'),
]
