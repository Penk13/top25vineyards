from django.shortcuts import get_list_or_404
from vineyards.models import Region
from .models import ContentPage
from news.models import Post


def base_variable(request):
    navbar_region = get_list_or_404(Region)
    travel_news = get_list_or_404(Post)
    footer_count = ContentPage.objects.filter(types="PAGE").count()
    footer_index = int(footer_count/2)
    footers1 = get_list_or_404(ContentPage, types="PAGE")[:footer_index]
    footers2 = get_list_or_404(ContentPage, types="PAGE")[footer_index:]
    return {"navbar_region": navbar_region,
            "travel_news": travel_news,
            "footers1": footers1,
            "footers2": footers2}
