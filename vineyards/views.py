from django.shortcuts import render, get_object_or_404
from .models import Vineyard


def vineyard_detail(request, pk):
    vineyard = get_object_or_404(Vineyard, pk=pk)
    context = {"vineyard": vineyard}
    return render(request, "vineyards/vineyard.html", context)


def vineyard_region(request):
    return render(request)
