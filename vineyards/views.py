from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Vineyard, Region


def vineyard_detail(request, pk):
    vineyard = get_object_or_404(Vineyard, pk=pk)
    context = {"vineyard": vineyard}
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request, slug):
    region = get_object_or_404(Region, slug=slug)
    p = Paginator(Vineyard.objects.filter(
        region=region).order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"vineyards": vineyards, "region": region}
    return render(request, "vineyards/vineyard_region.html", context)
