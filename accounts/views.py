from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from pages_app.models import ContentPage

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        print("POST")
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            print("VALID")
            form.save()
            return redirect("accounts:login")
    content_page = get_object_or_404(ContentPage, types="SEARCH_PAGE")
    context = {
        'user': user,
        'profile': profile,
        'content_page': content_page,
        'form': form,
    }
    return render(request, "account/profile.html", context)
