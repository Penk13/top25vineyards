from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import ContentPage
from vineyards.models import Vineyard


def mainpage(request):
    homepage = get_object_or_404(ContentPage, types="HOME_PAGE")
    p = Paginator(Vineyard.objects.all().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"homepage": homepage,
               "vineyards": vineyards}
    return render(request, "pages_app/main_page.html", context)


def footerpage(request, slug):
    page = get_object_or_404(ContentPage, slug=slug)
    context = {"page": page}
    return render(request, "pages_app/footer_page.html", context)
