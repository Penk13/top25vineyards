from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import ContentPage
from vineyards.models import Vineyard


def mainpage(request):
    homepage = get_object_or_404(ContentPage, pk=1)
    p = Paginator(Vineyard.objects.all(), 3)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"homepage": homepage, "vineyards": vineyards}
    return render(request, "pages_app/main_page.html", context)


def contact_us(request):
    context = {}
    return render(request, "pages_app/contact_us.html", context)


def about_us(request):
    context = {}
    return render(request, "pages_app/about_us.html", context)


def terms_of_service(request):
    context = {}
    return render(request, "pages_app/terms_of_service.html", context)


def privacy_statement(request):
    context = {}
    return render(request, "pages_app/privacy_statement.html", context)


def newsletter(request):
    context = {}
    return render(request, "pages_app/newsletter.html", context)


def advertise_with_us(request):
    context = {}
    return render(request, "pages_app/advertise_with_us.html", context)


def help_or_faq(request):
    context = {}
    return render(request, "pages_app/help_or_faq.html", context)


def site_map(request):
    context = {}
    return render(request, "pages_app/site_map.html", context)
