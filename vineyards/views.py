from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Vineyard, Region, RegionImage, YardImage, YardCoverImage


def vineyard_detail(request, pk):
    vineyard = get_object_or_404(Vineyard, pk=pk)
    yard_images = YardImage.objects.filter(vineyard=vineyard)
    yard_cover_images = YardCoverImage.objects.filter(vineyard=vineyard)
    context = {"vineyard": vineyard, "yard_images": yard_images,
               "yard_cover_images": yard_cover_images}
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request, slug):
    region = get_object_or_404(Region, slug=slug)
    region_images = RegionImage.objects.filter(region=region)
    p = Paginator(Vineyard.objects.filter(
        region=region).order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"vineyards": vineyards, "region": region,
               "region_images": region_images}
    return render(request, "vineyards/vineyard_region.html", context)
