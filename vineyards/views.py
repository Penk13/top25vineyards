from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Region, RegionChild, Vineyard
from news.models import Post
from pages_app.models import ContentPage


def vineyard_detail(request, pk):
    vineyard = get_object_or_404(Vineyard, pk=pk)
    travel_news = get_list_or_404(Post)
    footer_count = ContentPage.objects.filter(types="PAGE").count()
    footer_index = int(footer_count/2)
    footers1 = get_list_or_404(ContentPage, types="PAGE")[:footer_index]
    footers2 = get_list_or_404(ContentPage, types="PAGE")[footer_index:]
    context = {"vineyard": vineyard, "travel_news": travel_news,
               "footers1": footers1, "footers2": footers2}
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request):
    return render(request)
