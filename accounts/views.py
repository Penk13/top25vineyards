from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from pages_app.models import ContentPage
from vineyards.models import ReviewAndRating, Vineyard
from allauth.account.views import LoginView


@login_required
def profile(request):
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


# Override django allauth login view
class AccountLoginView(LoginView):
    def form_valid(self, form):
        if 'vineyard' in self.request.session:
            vineyard = Vineyard.objects.get(
                id=self.request.session['vineyard'])
            self.request.session.pop('vineyard')
            success_url = vineyard.get_absolute_url()+'form'
        else:
            success_url = self.get_success_url()
        try:
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response


account_login_view = AccountLoginView.as_view()
