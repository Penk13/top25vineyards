from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Region, RegionChild, Vineyard
from news.models import Post


def vineyard_detail(request, pk):
    vineyard = get_object_or_404(Vineyard, pk=pk)
    travel_news = get_list_or_404(Post)
    context = {"vineyard": vineyard, "travel_news": travel_news}
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request):
    return render(request)
