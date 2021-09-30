from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import ContentPage, ImageUpload
from vineyards.models import Vineyard

from mailing.models import ContactEntry, Subscriber
from mailing.forms import ContactEntryForm, SubscriberForm


def mainpage(request):
    homepage = get_object_or_404(ContentPage, types="HOME_PAGE")
    image_carousel = ImageUpload.objects.filter(page=homepage)
    p = Paginator(Vineyard.objects.all().order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"homepage": homepage,
               "vineyards": vineyards,
               "image_carousel": image_carousel}
    return render(request, "pages_app/main_page.html", context)


def footerpage(request, slug):
    page = get_object_or_404(ContentPage, slug=slug)
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

    context = {"page": page,
               "contact_entry_form": contact_entry_form,
               "subscriber_form": subscriber_form}
    return render(request, "pages_app/footer_page.html", context)


def searchpage(request):
    if request.method == "POST":
        searched = request.POST['searched']
        p = Paginator(Vineyard.objects.filter(
            text__icontains=searched).order_by("-rating"), 10)
        page = request.GET.get('page')
        vineyards = p.get_page(page)
    context = {"searched": searched, "vineyards": vineyards}
    return render(request, "pages_app/search_page.html", context)
