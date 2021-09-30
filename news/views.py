from django.shortcuts import render, get_object_or_404
from .models import Post


def news_detail(request, category, slug):
    news = get_object_or_404(Post, slug=slug)
    context = {"news": news}
    return render(request, "news/news.html", context)
