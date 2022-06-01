from django.http import JsonResponse
from django.template.loader import render_to_string
from vineyards.models import Vineyard
from .models import WineRegion, Country, WorldRegion, Wine, Facility, Service, Rating


def filter_data(request):
    defaultVineyards = request.GET.get('defaultVineyards')
    offset = int(request.GET['totalVineyards'])
    limit = int(request.GET['vineyardsPerPage'])
    world_region = request.GET.getlist('world_region[]')
    country = request.GET.getlist('country[]')
    wine_region = request.GET.getlist('wine_region[]')
    wine = request.GET.getlist('wine[]')
    facility = request.GET.getlist('facility[]')
    service = request.GET.getlist('service[]')
    rating = request.GET.getlist('rating[]')

    defaultVineyards = defaultVineyards.strip('][').split(', ')
    vineyardList = Vineyard.objects.filter(id__in=defaultVineyards)

    if len(wine_region) > 0:
        qs = WineRegion.objects.filter(id__in=wine_region).values_list('id', flat=True)
        vineyardList = vineyardList.filter(wineregion_filter__in=qs)
    elif len(country) > 0:
        qs = Country.objects.filter(id__in=country).values_list('wine_rg', flat=True)
        vineyardList = vineyardList.filter(wineregion_filter__in=qs)
    elif len(world_region) > 0:
        qs1 = WorldRegion.objects.filter(id__in=world_region).values_list('id', flat=True)
        qs2 = Country.objects.filter(worldregion__in=qs1).values_list('wine_rg', flat=True)
        vineyardList = vineyardList.filter(wineregion_filter__in=qs2)

    if len(wine) > 0:
        qs = Wine.objects.filter(id__in=wine).values_list('id', flat=True)
        vineyardList = vineyardList.filter(wine_filter__in=qs)
    if len(facility) > 0:
        qs = Facility.objects.filter(id__in=facility).values_list('id', flat=True)
        vineyardList = vineyardList.filter(facility_filter__in=qs)
    if len(service) > 0:
        qs = Service.objects.filter(id__in=service).values_list('id', flat=True)
        vineyardList = vineyardList.filter(service_filter__in=qs)
    if len(rating) > 0:
        qs = Rating.objects.filter(id__in=rating).values_list('id', flat=True)
        vineyardList = vineyardList.filter(rating_filter__in=qs)

    vineyardList = vineyardList.filter(display=True).distinct().order_by("-rating")
    vineyards_id = list(vineyardList.values_list('id', flat=True))

    vineyards = render_to_string("ajax/vineyard_list.html", {'vineyards': vineyardList, 'vineyards_id': vineyards_id})
    return JsonResponse({'data': vineyards})


def load_more_data(request):
    offset = int(request.GET['totalVineyards'])
    limit = int(request.GET['vineyardsPerPage'])
    vineyardList = Vineyard.objects.filter(display=True).distinct().order_by("-rating")[offset:offset+limit]
    vineyards = render_to_string("ajax/vineyard_list.html", {'vineyards': vineyardList})
    return JsonResponse({'data': vineyards})
