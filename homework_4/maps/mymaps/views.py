from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from random import randint


def index(request):
    name = request.GET.get('name')
    if name is None:
        name = 'Anon'
    ctx = {'name': name}
    return render(request, 'index.html', ctx)


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
