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
    context = {"homepage": homepage,
               "navbar_region": navbar_region,
               "vineyards": vineyards,
               "travel_news": travel_news}
    return render(request, "pages_app/main_page.html", context)


def contact_us(request):
    context = {}
    return render(request, "pages_app/contact_us.html", context)


def about_us(request):
    about_us = get_object_or_404(ContentPage, title="About Us")
    context = {"about_us": about_us}
    return render(request, "pages_app/about_us.html", context)


def terms_of_service(request):
    terms_of_service = get_object_or_404(ContentPage, title="Terms of Service")
    context = {"terms_of_service": terms_of_service}
    return render(request, "pages_app/terms_of_service.html", context)


def privacy_statement(request):
    privacy_statement = get_object_or_404(
        ContentPage, title="Privacy Statement")
    context = {"privacy_statement": privacy_statement}
    return render(request, "pages_app/privacy_statement.html", context)


def newsletter(request):
    context = {}
    return render(request, "pages_app/newsletter.html", context)


def advertise_with_us(request):
    advertise_with_us = get_object_or_404(
        ContentPage, title="Advertise with Us")
    context = {"advertise_with_us": advertise_with_us}
    return render(request, "pages_app/advertise_with_us.html", context)


def help_or_faq(request):
    help_or_faq = get_object_or_404(ContentPage, title="Help / FAQ")
    context = {"help_or_faq": help_or_faq}
    return render(request, "pages_app/help_or_faq.html", context)


def site_map(request):
    site_map = get_object_or_404(ContentPage, title="Site Map")
    context = {"site_map": site_map}
    return render(request, "pages_app/site_map.html", context)
