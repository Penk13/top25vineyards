from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Region, RegionChild, Vineyard


# def vineyard_list(request):
#     vineyards = get_list_or_404(Vineyard)
#     vineyard = get_object_or_404(Vineyard, pk=1)
#     context = {"vineyards": vineyards, "vineyard": vineyard}
#     return render(request, "vineyards/vineyards.html", context)
