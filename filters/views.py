from django.http import JsonResponse
from django.template.loader import render_to_string
from vineyards.models import Vineyard
from .models import WineRegion, Country, GeoRegion, WorldArea, Wine, Facility, Service, Rating


def filter_data(request):
    currentVineyards = request.GET.getlist('currentVineyards[]')
    world_area = request.GET.getlist('world_area[]')
    geo_region = request.GET.getlist('geo_region[]')
    country = request.GET.getlist('country[]')
    wine_region = request.GET.getlist('wine_region[]')
    wine = request.GET.getlist('wine[]')
    facility = request.GET.getlist('facility[]')
    service = request.GET.getlist('service[]')
    rating = request.GET.getlist('rating[]')

    vineyardList = Vineyard.objects.filter(id__in=currentVineyards).distinct()

    if len(wine_region) > 0:
        qs = WineRegion.objects.filter(id__in=wine_region).distinct().values_list('id', flat=True)
        for id in qs:
            vineyardList = vineyardList.filter(wineregion_filter=id)
    elif len(country) > 0:
        qs = Country.objects.filter(id__in=country).distinct().values_list('wine_rg', flat=True)
        for id in qs:
            vineyardList = vineyardList.filter(wineregion_filter=id)
    elif len(geo_region) > 0:
        qs1 = GeoRegion.objects.filter(id__in=geo_region).distinct().values_list('id', flat=True)
        qs2 = Country.objects.filter(id__in=qs1).distinct().values_list('wine_rg', flat=True)
        for id in qs2:
            vineyardList = vineyardList.filter(wineregion_filter=id)
    elif len(world_area) > 0:
        qs1 = WorldArea.objects.filter(id__in=world_area).distinct().values_list('id', flat=True)
        qs2 = GeoRegion.objects.filter(id__in=qs1).distinct().values_list('id', flat=True)
        qs3 = Country.objects.filter(id__in=qs2).distinct().values_list('wine_rg', flat=True)
        for id in qs3:
            vineyardList = vineyardList.filter(wineregion_filter=id)

    if len(wine) > 0:
        qs = Wine.objects.filter(id__in=wine).distinct().values_list('id', flat=True)
        for id in qs:
            vineyardList = vineyardList.filter(wine_filter=id)
    if len(facility) > 0:
        qs = Facility.objects.filter(id__in=facility).distinct().values_list('id', flat=True)
        for id in qs:
            vineyardList = vineyardList.filter(facility_filter=id)
    if len(service) > 0:
        qs = Service.objects.filter(id__in=service).distinct().values_list('id', flat=True)
        for id in qs:
            vineyardList = vineyardList.filter(service_filter=id)
    if len(rating) > 0:
        qs = Rating.objects.filter(id__in=rating).distinct().values_list('id', flat=True)
        for id in qs:
            vineyardList = vineyardList.filter(rating_filter=id)

    vineyards = render_to_string("ajax/vineyard_list.html", {'vineyards': vineyardList})
    return JsonResponse({'data': vineyards})


def load_more_data(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    vineyardList = Vineyard.objects.filter(display=True).distinct().order_by("-rating")[offset:offset+limit]
    vineyards = render_to_string("ajax/vineyard_list.html", {'vineyards': vineyardList})
    return JsonResponse({'data': vineyards})
