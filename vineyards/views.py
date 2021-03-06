from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Vineyard, Region, RegionImage, TopSliderImage, CoverSliderImage, ReviewAndRating, Comment
from .forms import ReviewRatingForm, VineyardForm
from datetime import date, timedelta
from django.core.mail import send_mail
from django.conf import settings
from list.models import Post, Category, Billboard


def vineyard_detail(request, region, slug, parent=None):
    vineyard = get_object_or_404(Vineyard, slug=slug, display=True)
    comments = Comment.objects.filter(approved=True)
    yard_images = TopSliderImage.objects.filter(vineyard=vineyard)
    yard_cover_images = CoverSliderImage.objects.filter(vineyard=vineyard)
    review_and_rating = ReviewAndRating.objects.filter(
        vineyard=vineyard, approved=True)
    recent_reviews = ReviewAndRating.objects.filter(
        vineyard=vineyard, approved=True).order_by('-id')[:3]

    # List Carousel
    list_carousel = Post.objects.filter(category__in=vineyard.list_carousel.all()).order_by("-id")
    billboards = Billboard.objects.filter(display=True)

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
               "comments": comments,
               "recent_reviews": recent_reviews,
               "error_msg": error_msg,
               "success_msg": success_msg,
               "list_carousel": list_carousel,
               "billboards": billboards,
               }
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request, region, parent=None):
    region = get_object_or_404(Region, slug=region)
    region_images = RegionImage.objects.filter(region=region)

    # List Section 1: Vineyard By Region
    p = Paginator(Vineyard.objects.filter(
        regions=region, display=True).order_by("-rating"), 10)
    page = request.GET.get('page')
    vineyards = p.get_page(page)

    # List Carousel
    list_carousel = Post.objects.filter(category__in=region.list_carousel.all()).order_by("-id")
    billboards = Billboard.objects.filter(display=True)

    context = {"region": region,
               "region_images": region_images,
               "vineyards": vineyards,
               "list_carousel": list_carousel,
               "billboards": billboards,
               }
    return render(request, "vineyards/vineyard_region.html", context)


def rr_form(request, region, slug, parent=None):
    vineyard = get_object_or_404(Vineyard, slug=slug)
    yard_images = TopSliderImage.objects.filter(vineyard=vineyard)
    yard_cover_images = CoverSliderImage.objects.filter(vineyard=vineyard)
    recent_reviews = ReviewAndRating.objects.filter(
        vineyard=vineyard, approved=True).order_by('-id')[:3]
    form = ReviewRatingForm(request.POST or None)

    # List Carousel: Global Travel News
    category = Category.objects.get(slug="global-travel-news")
    travel_news = Post.objects.filter(category=category).order_by("-id")
    billboards = Billboard.objects.filter(display=True)

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
               "travel_news": travel_news,
               "billboards": billboards,
               }
    return render(request, "vineyards/rr_form.html", context)


def edit_vineyard(request, vineyard):
    vineyard = get_object_or_404(Vineyard, slug=vineyard)

    # List Carousel: Global Travel News
    category = Category.objects.get(slug="global-travel-news")
    travel_news = Post.objects.filter(category=category).order_by("-id")
    billboards = Billboard.objects.filter(display=True)

    if vineyard.user == request.user:
        vineyard_form = VineyardForm(instance=vineyard)
        if request.user.is_authenticated:
            if request.method == "POST":
                vineyard_form = VineyardForm(request.POST, request.FILES, instance=vineyard)
                if vineyard_form.is_valid():
                    instance = vineyard_form.save(commit=False)
                    instance.display = False
                    instance.send_mail = False
                    instance.save()
                    vineyard_form.save_m2m()
                    # From Admin to User
                    subject = "Update Vineyard"
                    body = "Your vineyard updates have been recorded but have to be approved by Admin."
                    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [vineyard.email1])
                    # From User to Admin
                    subject = "Update Vineyard"
                    body = "Update Vineyard from User"
                    send_mail(subject, body, "", [settings.DEFAULT_FROM_EMAIL])
                    return redirect("mainpage")
    else:
        return redirect("mainpage")
    context = {"vineyard": vineyard,
                "vineyard_form": vineyard_form,
                "travel_news": travel_news,
                "billboards": billboards,
                }
    return render(request, "vineyards/edit_vineyard.html", context)
