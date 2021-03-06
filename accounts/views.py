from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from pages_app.models import ContentPage
from vineyards.models import ReviewAndRating, Vineyard
from vineyards.forms import CommentForm
from datetime import date, timedelta


@login_required
def profile(request):
    # From submit_vineyard
    if 'submit_vineyard' in request.session:
        request.session.pop('submit_vineyard')
        return redirect("footerpage", slug="submit-a-vineyard")

    # From rr_form
    if 'vineyard' in request.session:
        vineyard = Vineyard.objects.get(
            id=request.session['vineyard'])
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

        if not allowed:
            request.session['rr_form_error_msg'] = "Sorry you can't post right now. You have to wait 10 days since the last post."
        else:
            request.session['rr_form'].pop('captcha')
            request.session.modified = True
            ReviewAndRating.objects.create(user=request.user, vineyard=vineyard, **request.session["rr_form"])
            request.session['rr_form_success_msg'] = "Your Rating and Review has been submitted. Thank you."
        request.session.pop('vineyard')
        request.session.pop('rr_form')
        return redirect(vineyard.get_absolute_url())

    user = request.user
    profile = Profile.objects.get(user=user)
    vineyards = Vineyard.objects.filter(user=user)
    rr_received = ReviewAndRating.objects.filter(vineyard__in=vineyards)

    # Profile Form
    form = ProfileForm(instance=profile)
    review_and_rating = ReviewAndRating.objects.filter(
        user=user, approved=True)
    if request.method == 'POST' and 'profile_form' in request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")

    # Comment Form
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid() and 'comment_form' in request.POST:
        rr = ReviewAndRating.objects.get(pk=request.POST['rr_id'])
        instance = comment_form.save(commit=False)
        instance.user = request.user
        instance.rr = rr
        instance.save()
        return redirect("profile")

    content_page = get_object_or_404(ContentPage, types="SEARCH_PAGE")
    context = {
        'user': user,
        'profile': profile,
        'content_page': content_page,
        'form': form,
        'review_and_rating': review_and_rating,
        'vineyards': vineyards,
        'rr_received': rr_received,
        'comment_form': comment_form,
    }
    return render(request, "account/profile.html", context)
