from django.shortcuts import get_list_or_404
from .models import ContentPage
from vineyards.models import Region
from news.models import Post


def base_variable(request):
    navbar_region = Region.objects.filter(
        display_on_navbar=True, region_parent=None)
    navbar_region_child = Region.objects.filter(
        display_on_navbar=True, region_parent=True)
    travel_news = Post.objects.all()
    footer_count = ContentPage.objects.filter(types="PAGE").count()
    footer_index = int(footer_count/2)
    footers1 = get_list_or_404(ContentPage, types="PAGE")[:footer_index]
    footers2 = get_list_or_404(ContentPage, types="PAGE")[footer_index:]
    return {"navbar_region": navbar_region,
            "navbar_region_child": navbar_region_child,
            "travel_news": travel_news,
            "footers1": footers1,
            "footers2": footers2}
