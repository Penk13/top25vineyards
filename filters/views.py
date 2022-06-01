from django.http import JsonResponse
from django.template.loader import render_to_string
from vineyards.models import Vineyard
from .models import WineRegion, Country, WorldRegion, Wine, Facility, Service, Rating


def filter_data(request):
    defaultVineyards = request.GET.get('defaultVineyards')
    total_vineyards = int(request.GET['totalVineyards'])
    vineyards_per_page = int(request.GET['vineyardsPerPage'])
    vineyard_pages = int(request.GET['vineyardPages'])

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

    vineyards_qs = vineyardList.filter(display=True).distinct().order_by("-rating")
    vineyards = vineyards_qs
    vineyards_id = list(vineyards_qs.values_list('id', flat=True))

    data = render_to_string("ajax/vineyard_list.html", {
        "vineyards_per_page": vineyards_per_page,
        "vineyards": vineyards,
        "total_vineyards": total_vineyards,
        "vineyards_id": vineyards_id,
        "vineyard_pages": vineyard_pages,
    })
    return JsonResponse({'data': data})


def load_more_data(request):
    currentVineyards = request.GET.get('currentVineyards')
    total_vineyards = int(request.GET['totalVineyards'])
    vineyards_per_page = int(request.GET['vineyardsPerPage'])
    vineyard_pages = int(request.GET['vineyardPages'])

    currentVineyards = currentVineyards.strip('][').split(', ')
    vineyards_qs = Vineyard.objects.filter(display=True).distinct().order_by("-rating")
    vineyards = vineyards_qs
    vineyards_id = list(vineyards_qs.values_list('id', flat=True))

    data = render_to_string("ajax/vineyard_list.html", {
        "vineyards_per_page": vineyards_per_page,
        "vineyards": vineyards,
        "total_vineyards": total_vineyards,
        "vineyards_id": vineyards_id,
        "vineyard_pages": vineyard_pages,
    })
    return JsonResponse({'data': data})
