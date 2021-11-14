from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from pages_app.models import ContentPage
from vineyards.models import ReviewAndRating, Vineyard
from vineyards.forms import ReviewRatingForm


@login_required
def profile(request):
    if 'vineyard' in request.session:
        vineyard = Vineyard.objects.get(
            id=request.session['vineyard'])
        # If it's update form
        try:
            obj = ReviewAndRating.objects.get(
                user=request.user, vineyard=vineyard)
            form = ReviewRatingForm(request.session['rr_form'], instance=obj)
            obj.approved = False
            form.save()
        # If not update form
        except:
            obj = None
            form = ReviewRatingForm(request.session['rr_form'])
            instance = form.save(commit=False)
            instance.user = request.user
            instance.vineyard = vineyard
            instance.save()
        request.session.pop('vineyard')
        request.session.pop('rr_form')
        return redirect(vineyard.get_absolute_url())
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    review_and_rating = ReviewAndRating.objects.filter(
        user=user, approved=True)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    content_page = get_object_or_404(ContentPage, types="SEARCH_PAGE")
    context = {
        'user': user,
        'profile': profile,
        'content_page': content_page,
        'form': form,
        'review_and_rating': review_and_rating,
    }
    return render(request, "account/profile.html", context)
