from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import ContentPage
from vineyards.models import Vineyard, Region
from news.models import Post


def mainpage(request):
    homepage = get_object_or_404(ContentPage, types="HOME_PAGE")
    navbar_region = get_list_or_404(Region)
    p = Paginator(Vineyard.objects.all().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    travel_news = get_list_or_404(Post)
    footer_count = ContentPage.objects.filter(types="PAGE").count()
    footer_index = int(footer_count/2)
    footers1 = get_list_or_404(ContentPage, types="PAGE")[:footer_index]
    footers2 = get_list_or_404(ContentPage, types="PAGE")[footer_index:]
    context = {"homepage": homepage,
               "navbar_region": navbar_region,
               "vineyards": vineyards,
               "travel_news": travel_news,
               "footers1": footers1,
               "footers2": footers2}
    return render(request, "pages_app/main_page.html", context)


def footerpage(request, slug):
    page = get_object_or_404(ContentPage, slug=slug)
    travel_news = get_list_or_404(Post)
    footer_count = ContentPage.objects.filter(types="PAGE").count()
    footer_index = int(footer_count/2)
    footers1 = get_list_or_404(ContentPage, types="PAGE")[:footer_index]
    footers2 = get_list_or_404(ContentPage, types="PAGE")[footer_index:]
    context = {"page": page, "travel_news": travel_news,
               "footers1": footers1, "footers2": footers2}
    return render(request, "pages_app/footer_page.html", context)
