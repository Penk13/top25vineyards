from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Vineyard, Region, RegionImage, TopSliderImage, CoverSliderImage, ReviewAndRating
from .forms import ReviewRatingForm


def vineyard_detail(request, region, slug, parent=None):
    vineyard = get_object_or_404(Vineyard, slug=slug)
    yard_images = TopSliderImage.objects.filter(vineyard=vineyard)
    yard_cover_images = CoverSliderImage.objects.filter(vineyard=vineyard)
    review_and_rating = ReviewAndRating.objects.filter(vineyard=vineyard)
    try:
        obj = ReviewAndRating.objects.get(user=request.user, vineyard=vineyard)
        form = ReviewRatingForm(request.POST or None, instance=obj)
    except:
        obj = None
        form = ReviewRatingForm(request.POST or None)
    if form.is_valid():
        if obj:
            form.save()
        else:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.vineyard = vineyard
            instance.save()
        # form = ReviewRatingForm()
    context = {"vineyard": vineyard,
               "yard_images": yard_images,
               "yard_cover_images": yard_cover_images,
               "review_and_rating": review_and_rating,
               "form": form,
               }
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request, slug):
    region = get_object_or_404(Region, slug=slug)
    region_images = RegionImage.objects.filter(region=region)
    p = Paginator(Vineyard.objects.filter(
        regions=region).order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)
    context = {"vineyards": vineyards, "region": region,
               "region_images": region_images}
    return render(request, "vineyards/vineyard_region.html", context)
