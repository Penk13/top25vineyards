from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ContentPage, ImageUpload
from vineyards.models import Vineyard, Region
from vineyards.forms import VineyardUserForm, VineyardForm
from news.models import Post, Category

from mailing.models import ContactEntry, Subscriber
from mailing.forms import ContactEntryForm, SubscriberForm

from itertools import chain


def mainpage(request):
    content_page = get_object_or_404(ContentPage, types="HOME_PAGE")
    image_carousel = ImageUpload.objects.filter(page=content_page)
    if content_page.category:
        p = Paginator(Vineyard.objects.filter(
            regions=content_page.category, display=True).order_by("-rating"), 10)
    else:
        p = Paginator(Vineyard.objects.filter(display=True).order_by("-rating"), 10)
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
    vineyard_form = VineyardForm()
    vineyard_user_form = VineyardUserForm()

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

    elif slug == "submit-vineyard":
        vineyard_form = VineyardForm()
        vineyard_user_form = VineyardUserForm()
        if request.user.is_authenticated:
            if request.method == "POST":
                vineyard_form = VineyardForm(request.POST,request.FILES)
                vineyard_user_form = VineyardUserForm(request.POST)
                if vineyard_form.is_valid() and vineyard_user_form.is_valid():
                    instance1 = vineyard_form.save(commit=False)
                    instance1.save()
                    instance2 = vineyard_user_form.save(commit=False)
                    instance2.vineyard = instance1
                    instance2.name = request.user.username
                    instance2.email1 = request.user.email
                    instance2.save()
                    return redirect("pages_app:mainpage")
        else:
            request.session["v_form"] = True
            return redirect("account_login")

    context = {"content_page": content_page,
               "contact_entry_form": contact_entry_form,
               "subscriber_form": subscriber_form,
               "vineyard_form": vineyard_form,
               "vineyard_user_form": vineyard_user_form}
    return render(request, "pages_app/footer_page.html", context)


def searchpage(request):
    content_page = get_object_or_404(ContentPage, types="SEARCH_PAGE")
    if request.method == "POST":
        searched = request.POST['searched']
    else:
        searched = request.GET.get('searched')
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
    regions = Region.objects.filter(
        Q(name__icontains=searched) |
        Q(title__icontains=searched) |
        Q(description__icontains=searched)
    )
    pages = ContentPage.objects.filter(
        Q(content__icontains=searched) |
        Q(additional_content__icontains=searched)
    )
    result_list = list(chain(vineyard, news, regions, pages))
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
            regions=content_page.category, display=True).order_by("-rating"), 10)
    else:
        p = Paginator(Vineyard.objects.filter(display=True).order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"content_page": content_page,
               "vineyards": vineyards,
               "image_carousel": image_carousel}
    return render(request, "pages_app/page.html", context)


def newspage(request, slug):
    content_page = get_object_or_404(ContentPage, slug=slug)
    image_carousel = ImageUpload.objects.filter(page=content_page)
    category = Category.objects.get(slug=content_page.slug)
    p = Paginator(Post.objects.filter(category=category).order_by("-id"), 10)
    page = request.GET.get('page')
    news_list = p.get_page(page)
    context = {"content_page": content_page,
               "image_carousel": image_carousel,
               "news_list": news_list}
    return render(request, "pages_app/newspage.html", context)
