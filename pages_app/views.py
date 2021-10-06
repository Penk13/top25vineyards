from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ContentPage, ImageUpload
from vineyards.models import Vineyard
from news.models import Post

from mailing.models import ContactEntry, Subscriber
from mailing.forms import ContactEntryForm, SubscriberForm

from itertools import chain


def mainpage(request):
    content_page = get_object_or_404(ContentPage, types="HOME_PAGE")
    image_carousel = ImageUpload.objects.filter(page=content_page)
    if content_page.category:
        p = Paginator(Vineyard.objects.filter(
            regions=content_page.category).order_by("-rating"), 10)
    else:
        p = Paginator(Vineyard.objects.all().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"content_page": content_page,
               "vineyards": vineyards,
               "image_carousel": image_carousel}
    return render(request, "pages_app/main_page.html", context)


def footerpage(request, slug):
    content_page = get_object_or_404(ContentPage, slug=slug)
    contact_entry_form = ContactEntryForm()
    subscriber_form = SubscriberForm()

    if slug == "contact-us":
        contact_entry_form = ContactEntryForm()
        if request.method == "POST":
            contact_entry_form = ContactEntryForm(request.POST)
            if contact_entry_form.is_valid():
                ContactEntry.objects.create(**contact_entry_form.cleaned_data)
            return redirect("pages_app:mainpage")

    elif slug == "newsletter":
        subscriber_form = SubscriberForm()
        if request.method == "POST":
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                Subscriber.objects.create(**subscriber_form.cleaned_data)
            return redirect("pages_app:mainpage")

    context = {"content_page": content_page,
               "contact_entry_form": contact_entry_form,
               "subscriber_form": subscriber_form}
    return render(request, "pages_app/footer_page.html", context)


def searchpage(request):
    content_page = get_object_or_404(ContentPage, types="SEARCH_PAGE")
    if request.method == "POST":
        searched = request.POST['searched']
        vineyard = Vineyard.objects.filter(
            Q(name__icontains=searched) |
            Q(text__icontains=searched) |
            Q(wine_rg__icontains=searched) |
            Q(wines__icontains=searched) |
            Q(grapes__icontains=searched) |
            Q(owner__icontains=searched)
        ).order_by("-rating")
        news = Post.objects.filter(
            Q(title__icontains=searched) |
            Q(body__icontains=searched)
        )
        result_list = list(chain(vineyard, news))
        p = Paginator(result_list, 10)
        page = request.GET.get('page')
        results = p.get_page(page)
    context = {"content_page": content_page,
               "searched": searched, "results": results}
    return render(request, "pages_app/search_page.html", context)


def page(request, slug):
    content_page = get_object_or_404(ContentPage, slug=slug)
    image_carousel = ImageUpload.objects.filter(page=content_page)
    if content_page.category:
        p = Paginator(Vineyard.objects.filter(
            regions=content_page.category).order_by("-rating"), 10)
    else:
        p = Paginator(Vineyard.objects.all().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"content_page": content_page,
               "vineyards": vineyards,
               "image_carousel": image_carousel}
    return render(request, "pages_app/page.html", context)


def travel_news_page(request):
    content_page = get_object_or_404(ContentPage, types="GLOBAL_TRAVEL_NEWS")
    p = Paginator(Post.objects.all(), 10)
    page = request.GET.get('page')
    travel_news = p.get_page(page)
    context = {"content_page": content_page,
               "travel_news": travel_news,
               }
    return render(request, "pages_app/newspage.html", context)
