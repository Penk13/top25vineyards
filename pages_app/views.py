from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ContentPage, ImageUpload
from vineyards.models import Vineyard, Region
from vineyards.forms import VineyardForm
from news.models import Post, Category, Billboard

from mailing.models import ContactEntry, Subscriber
from mailing.forms import ContactEntryForm, SubscriberForm

from itertools import chain


def mainpage(request):
    content_page = get_object_or_404(ContentPage, types="HOME_PAGE")
    news = Post.objects.filter(category__in=content_page.news.all()).order_by("-id")
    billboards = Billboard.objects.filter(display=True)
    image_carousel = ImageUpload.objects.filter(page=content_page)
    p = Paginator(Vineyard.objects.filter(
        regions__in=content_page.category.all(), display=True).distinct().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"content_page": content_page,
               "vineyards": vineyards,
               "image_carousel": image_carousel,
               "news": news,
               "billboards": billboards,
               }
    # Popup message if the form is submitted successfully
    if("contact_form_msg" in request.session):
        context["msg"] = request.session["contact_form_msg"]
        request.session.pop("contact_form_msg")
    if("subscribe_form_msg" in request.session):
        context["msg"] = request.session["subscribe_form_msg"]
        request.session.pop("subscribe_form_msg")
    if("vineyard_form_msg" in request.session):
        context["msg"] = request.session["vineyard_form_msg"]
        request.session.pop("vineyard_form_msg")
    return render(request, "pages_app/main_page.html", context)


def footerpage(request, slug):
    content_page = get_object_or_404(ContentPage, slug=slug)
    news = Post.objects.filter(category__in=content_page.news.all()).order_by("-id")
    billboards = Billboard.objects.filter(display=True)

    p = Paginator(Vineyard.objects.filter(
        regions__in=content_page.category.all(), display=True).distinct().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)

    contact_entry_form = ContactEntryForm()
    subscriber_form = SubscriberForm()
    vineyard_form = VineyardForm()

    if slug == "contact-us":
        contact_entry_form = ContactEntryForm()
        if request.method == "POST":
            contact_entry_form = ContactEntryForm(request.POST)
            if contact_entry_form.is_valid():
                ContactEntry.objects.create(
                    name = contact_entry_form.cleaned_data["name"],
                    email = contact_entry_form.cleaned_data["email"],
                    subject = contact_entry_form.cleaned_data["subject"],
                    message = contact_entry_form.cleaned_data["message"])
                request.session["contact_form_msg"] = "Your message has been sent! Thank you!"
                return redirect("pages_app:mainpage")

    elif slug == "newsletter":
        subscriber_form = SubscriberForm()
        if request.method == "POST":
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                Subscriber.objects.create(
                    name = subscriber_form.cleaned_data["name"],
                    email = subscriber_form.cleaned_data["email"],
                    country = subscriber_form.cleaned_data["country"])
                request.session["subscribe_form_msg"] = "Thanks for subscribing to our newsletter!"
                return redirect("pages_app:mainpage")

    elif slug == "submit-a-vineyard":
        vineyard_form = VineyardForm()
        if request.user.is_authenticated:
            if request.method == "POST":
                vineyard_form = VineyardForm(request.POST, request.FILES)
                if vineyard_form.is_valid():
                    instance = vineyard_form.save(commit=False)
                    instance.user = request.user
                    instance.email1 = request.user.email
                    instance.save()
                    vineyard_form.save_m2m()
                    request.session["vineyard_form_msg"] = "Your vineyard has been successfully submitted!"
                    return redirect("pages_app:mainpage")
        else:
            request.session["submit_vineyard"] = True
            return redirect("account_login")

    context = {"content_page": content_page,
               "vineyards": vineyards,
               "contact_entry_form": contact_entry_form,
               "subscriber_form": subscriber_form,
               "vineyard_form": vineyard_form,
               "news": news,
               "billboards": billboards,
               }
    return render(request, "pages_app/footer_page.html", context)


def searchpage(request):
    content_page = get_object_or_404(ContentPage, types="SEARCH_PAGE")
    news = Post.objects.filter(category__in=content_page.news.all()).order_by("-id")
    billboards = Billboard.objects.filter(display=True)

    p = Paginator(Vineyard.objects.filter(
        regions__in=content_page.category.all(), display=True).distinct().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)

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
        Q(owner__icontains=searched) |
        Q(meta_description__icontains=searched) |
        Q(meta_keywords__icontains=searched)
    ).order_by("-rating")
    news = Post.objects.filter(
        Q(title__icontains=searched) |
        Q(body__icontains=searched) |
        Q(meta_description__icontains=searched) |
        Q(meta_keywords__icontains=searched)
    ).order_by("-id")
    regions = Region.objects.filter(
        Q(name__icontains=searched) |
        Q(title__icontains=searched) |
        Q(description__icontains=searched) |
        Q(meta_description__icontains=searched) |
        Q(meta_keywords__icontains=searched)
    )
    pages = ContentPage.objects.filter(
        Q(content__icontains=searched) |
        Q(additional_content__icontains=searched) |
        Q(meta_description__icontains=searched) |
        Q(meta_keywords__icontains=searched)
    )
    result_list = list(chain(vineyard, news, regions, pages))
    p = Paginator(result_list, 10)
    page = request.GET.get('page')
    results = p.get_page(page)
    context = {"content_page": content_page,
               "vineyards": vineyards,
               "searched": searched,
               "results": results,
               "news": news,
               "billboards": billboards,
               }
    return render(request, "pages_app/search_page.html", context)


def page(request, slug):
    content_page = get_object_or_404(ContentPage, slug=slug)    
    news = Post.objects.filter(category__in=content_page.news.all()).order_by("-id")
    billboards = Billboard.objects.filter(display=True)
    image_carousel = ImageUpload.objects.filter(page=content_page)
    p = Paginator(Vineyard.objects.filter(
        regions__in=content_page.category.all(), display=True).distinct().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"content_page": content_page,
               "vineyards": vineyards,
               "image_carousel": image_carousel,
               "news": news,
               "billboards": billboards,
               }
    return render(request, "pages_app/page.html", context)


def newspage(request, slug):
    content_page = get_object_or_404(ContentPage, slug=slug)
    news = Post.objects.filter(category__in=content_page.news.all()).order_by("-id")
    billboards = Billboard.objects.filter(display=True)

    p = Paginator(Vineyard.objects.filter(
        regions__in=content_page.category.all(), display=True).distinct().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)

    image_carousel = ImageUpload.objects.filter(page=content_page)
    category = Category.objects.get(slug=content_page.slug)
    p = Paginator(Post.objects.filter(category=category).order_by("-id"), 10)
    page = request.GET.get('page')
    news_list = p.get_page(page)
    context = {"content_page": content_page,
               "vineyards": vineyards,
               "image_carousel": image_carousel,
               "news_list": news_list,
               "news": news,
               "billboards": billboards,
               }
    return render(request, "pages_app/newspage.html", context)
