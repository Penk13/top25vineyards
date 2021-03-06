from django.http import JsonResponse
from django.template.loader import render_to_string
from vineyards.models import Vineyard
from .models import WineRegion, Country, WorldRegion, Wine, Facility, Service, Rating


def filter_data(request):
    world_region = request.GET.getlist('world_region[]')
    country = request.GET.getlist('country[]')
    wine_region = request.GET.getlist('wine_region[]')
    wine = request.GET.getlist('wine[]')
    facility = request.GET.getlist('facility[]')
    service = request.GET.getlist('service[]')
    rating = request.GET.getlist('rating[]')

    currentVineyards = request.GET.get('defaultVineyards')
    currentVineyards = currentVineyards.strip('][').split(', ')
    vineyardList = Vineyard.objects.filter(id__in=currentVineyards)

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
    total_vineyards = vineyards_qs.count()
    vineyards_id = list(vineyards_qs.values_list('id', flat=True))

    # Pagination
    per_page = int(request.GET.get('perPage'))
    num_pages = int(total_vineyards/per_page) + (total_vineyards % per_page > 0)
    current_page = 1
    page_range = [i for i in range(1, num_pages + 1)]

    vineyards = vineyards_qs[((current_page-1)*per_page):(current_page*per_page)]

    data = render_to_string("ajax/vineyard_list.html", {
        "vineyards": vineyards,
        "vineyards_id": vineyards_id,
        "per_page": per_page,
        "num_pages": num_pages,
        "current_page": current_page,
        "page_range": page_range,
    })
    return JsonResponse({'data': data, 'total_vineyards': total_vineyards})


def load_more_data(request):
    currentVineyards = request.GET.get('currentVineyards')

    currentVineyards = currentVineyards.strip('][').split(', ')
    vineyards_qs = Vineyard.objects.filter(id__in=currentVineyards, display=True).distinct().order_by("-rating")
    total_vineyards = vineyards_qs.count()
    vineyards_id = list(vineyards_qs.values_list('id', flat=True))

    # Pagination
    per_page = int(request.GET.get('perPage'))
    num_pages = int(total_vineyards/per_page) + (total_vineyards % per_page > 0)
    current_page = int(request.GET.get('currentPage'))
    page_range = [i for i in range(1, num_pages + 1)]

    vineyards = vineyards_qs[((current_page-1)*per_page):(current_page*per_page)]

    data = render_to_string("ajax/vineyard_list.html", {
        "vineyards": vineyards,
        "vineyards_id": vineyards_id,
        "per_page": per_page,
        "num_pages": num_pages,
        "current_page": current_page,
        "page_range": page_range,
    })
    return JsonResponse({'data': data, 'total_vineyards': total_vineyards})


def count_vineyards(request):
    currentVineyards = request.GET.get('currentVineyards')
    currentVineyards = currentVineyards.strip('][').split(', ')

    world_region = WorldRegion.objects.all().order_by("order")
    country = Country.objects.all().order_by("name")
    wine_region = WineRegion.objects.all().order_by("name")
    wine = Wine.objects.all().order_by("name")
    facility = Facility.objects.all().order_by("name")
    service = Service.objects.all().order_by("name")
    rating = Rating.objects.all().order_by("order")

    count_list = []
    for i in rating:
        vineyardList = Vineyard.objects.filter(id__in=currentVineyards)
        vineyardList = vineyardList.filter(rating_filter=i)
        vineyards_qs = vineyardList.filter(display=True).distinct()
        count_list.append(vineyards_qs.count())

    for i in world_region:
        vineyardList = Vineyard.objects.filter(id__in=currentVineyards)
        qs2 = Country.objects.filter(worldregion=i).values_list('wine_rg', flat=True)
        vineyardList = vineyardList.filter(wineregion_filter__in=qs2)
        vineyards_qs = vineyardList.filter(display=True).distinct()
        count_list.append(vineyards_qs.count())

    for i in country:
        vineyardList = Vineyard.objects.filter(id__in=currentVineyards)
        qs = WineRegion.objects.filter(country=i).values_list('id', flat=True)
        vineyardList = vineyardList.filter(wineregion_filter__in=qs)
        vineyards_qs = vineyardList.filter(display=True).distinct()
        count_list.append(vineyards_qs.count())

    for i in wine_region:
        vineyardList = Vineyard.objects.filter(id__in=currentVineyards)
        vineyardList = vineyardList.filter(wineregion_filter=i)
        vineyards_qs = vineyardList.filter(display=True).distinct()
        count_list.append(vineyards_qs.count())

    for i in wine:
        vineyardList = Vineyard.objects.filter(id__in=currentVineyards)
        vineyardList = vineyardList.filter(wine_filter=i)
        vineyards_qs = vineyardList.filter(display=True).distinct()
        count_list.append(vineyards_qs.count())

    for i in facility:
        vineyardList = Vineyard.objects.filter(id__in=currentVineyards)
        vineyardList = vineyardList.filter(facility_filter=i)
        vineyards_qs = vineyardList.filter(display=True).distinct()
        count_list.append(vineyards_qs.count())

    for i in service:
        vineyardList = Vineyard.objects.filter(id__in=currentVineyards)
        vineyardList = vineyardList.filter(service_filter=i)
        vineyards_qs = vineyardList.filter(display=True).distinct()
        count_list.append(vineyards_qs.count())

    count_result = count_list + count_list
    return JsonResponse({'count_result': count_result})
