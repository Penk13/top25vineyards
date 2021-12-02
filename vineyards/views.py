from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Vineyard, Region, RegionImage, TopSliderImage, CoverSliderImage, ReviewAndRating
from .forms import ReviewRatingForm
from datetime import date, timedelta


def vineyard_detail(request, region, slug, parent=None):
    vineyard = get_object_or_404(Vineyard, slug=slug)
    yard_images = TopSliderImage.objects.filter(vineyard=vineyard)
    yard_cover_images = CoverSliderImage.objects.filter(vineyard=vineyard)
    review_and_rating = ReviewAndRating.objects.filter(
        vineyard=vineyard, approved=True)
    recent_reviews = ReviewAndRating.objects.filter(
        vineyard=vineyard, approved=True).order_by('-id')[:3]
    error_msg = None
    success_msg = None
    if "rr_form_error_msg" in request.session:
        error_msg = request.session["rr_form_error_msg"]
        request.session.pop("rr_form_error_msg")
    elif "rr_form_success_msg" in request.session:
        success_msg = request.session["rr_form_success_msg"]
        request.session.pop("rr_form_success_msg")
    context = {"vineyard": vineyard,
               "yard_images": yard_images,
               "yard_cover_images": yard_cover_images,
               "review_and_rating": review_and_rating,
               "recent_reviews": recent_reviews,
               "error_msg": error_msg,
               "success_msg": success_msg
               }
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request, region, parent=None):
    region = get_object_or_404(Region, slug=region)
    region_images = RegionImage.objects.filter(region=region)
    p = Paginator(Vineyard.objects.filter(
        regions=region).order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"vineyards": vineyards, "region": region,
               "region_images": region_images}
    return render(request, "vineyards/vineyard_region.html", context)


def rr_form(request, region, slug, parent=None):
    vineyard = get_object_or_404(Vineyard, slug=slug)
    yard_images = TopSliderImage.objects.filter(vineyard=vineyard)
    yard_cover_images = CoverSliderImage.objects.filter(vineyard=vineyard)
    recent_reviews = ReviewAndRating.objects.filter(
        vineyard=vineyard, approved=True).order_by('-id')[:3]
    form = ReviewRatingForm(request.POST or None)

    # Check if there is a previous review
    try:
        obj = ReviewAndRating.objects.filter(
            user=request.user, vineyard=vineyard).latest('date_created')
        wait = obj.date_created.date() + timedelta(days=10)
        if date.today() < wait:
            allowed = False
        else:
            allowed = True
    except:
        allowed = True

    if form.is_valid():
        if not allowed:
            request.session['rr_form_error_msg'] = "Sorry you can't post right now. You have to wait 10 days since the last post."
        else:
            if request.user.is_authenticated:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.vineyard = vineyard
                instance.save()
                request.session['rr_form_success_msg'] = "Your Rating and Review has been submitted. Thank you."
            else:
                request.session['rr_form'] = form.cleaned_data
                request.session['vineyard'] = vineyard.id
                return redirect('account_login')
        return redirect(vineyard.get_absolute_url())
    context = {"vineyard": vineyard,
               "yard_images": yard_images,
               "yard_cover_images": yard_cover_images,
               "recent_reviews": recent_reviews,
               "form": form,
               }
    return render(request, "vineyards/rr_form.html", context)
