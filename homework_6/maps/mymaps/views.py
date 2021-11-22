from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.views.decorators.http import require_GET

from .models import Cities


def index(request):
    name = request.GET.get('name')
    if name is None:
        name = 'Anon'
    ctx = {'name': name}
    return render(request, 'index.html', ctx)


def create(request, name=None, lt=None, lg=None):
    new_city = Cities.objects.create(name=name, lt=lt, lg=lg)
    return JsonResponse(
        {
            'New city':
                {
                    'name': new_city.name,
                    'lt': new_city.lt,
                    'lg': new_city.lg
                }
        }
    )


@require_GET
def detail(request, city_id=None):
    queryset = Cities.objects.all()
    city = get_object_or_404(queryset, pk=city_id)
    return JsonResponse(
        {
            'city': city.name,
            'lt': city.lt,
            'lg': city.lg
        }
    )


@require_GET
def all_cities(request):
    cities = Cities.objects.all()
    data = [
        {
            'name': city.name,
            'lt': city.lt,
            'lg': city.lg
        } for city in cities
    ]
    return JsonResponse({'cities': data})


def change_name(request, city_id=None, new_name=None):
    queryset = Cities.objects.all()
    city = get_object_or_404(queryset, pk=city_id)
    old_name = city.name
    city.name = new_name
    city.save(update_fields=["name"])
    return JsonResponse({'data':
        [
            {
                'Old data':
                    {
                        'name': old_name,
                        'lt': city.lt,
                        'lg': city.lg}},
            {
                'Updated data':
                    {
                        'name': city.name,
                        'lt': city.lt,
                        'lg': city.lg
                    }
            }
        ]
    }
    )


def delete_city(request, city_id=None):
    queryset = Cities.objects.all()
    city = get_object_or_404(queryset, pk=city_id)
    city.delete()
    return JsonResponse(
        {'Удален':
            {
                'name': city.name,
                'lt': city.lt,
                'lg': city.lg
            }
        }
    )
