# import requests
# from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Autoblogging


def news_detail(request, category, news):
    news = get_object_or_404(Post, slug=news)
    context = {"news": news}
    return render(request, "news/news.html", context)


def autoblogging(request):
    sources = Autoblogging.objects.all()
    context = {"sources": sources}
    return render(request, "news/autoblogging.html", context)
