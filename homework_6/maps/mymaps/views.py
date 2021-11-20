from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from random import randint

from .models import Cities


def index(request):
    name = request.GET.get('name')
    if name is None:
        name = 'Anon'
    ctx = {'name': name}
    return render(request, 'index.html', ctx)


def create(request, name='new_city', lt=0, lg=0):
    # if not (isinstance(lt, int) or isinstance(lg, int)):
    #     return HttpResponse(status=400)
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
def detail(request, city_id=1):
    city = Cities.objects.all().filter(pk=city_id)[0]
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


def change_name(request, city_id=1, new_name='changed_name'):
    city = Cities.objects.get(pk=city_id)
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


def delete_city(request, city_id=1):
    city = Cities.objects.get(pk=city_id)
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


def map_detail(request):
    if request.method == 'POST':
        return HttpResponse(status=405)
    city = request.GET.get('city')
    if city is None:
        return JsonResponse({'City': 'No city'})
    return JsonResponse({city: {'lt': randint(-90, 90), 'lg': randint(-180, 180)}})


def map_create(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    city = request.GET.get('city')
    lt = request.GET.get('lt')
    lg = request.GET.get('lg')
    if None in (city, lt, lg):
        return HttpResponse(status=400)
    else:
        return JsonResponse({city: {'lt': lt, 'lg': lg}})


def map_list(request):
    if request.method == 'POST':
        return HttpResponse(status=405)
    return JsonResponse({'MSC': {'lt': 55.7334, 'lg': 37.6548}, 'TMN': {'lt': 53.1312, 'lg': 65.5483}})
