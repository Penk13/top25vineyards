import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Autoblogging, Category


def news_detail(request, category, news):
    news = get_object_or_404(Post, slug=news)
    context = {"news": news}
    return render(request, "news/news.html", context)


def autoblogging(request):
    sources = Autoblogging.objects.all()
    context = {"sources": sources}
    return render(request, "news/autoblogging.html", context)


def pull_feeds(request, pk):
    source = Autoblogging.objects.get(pk=pk)

    url = requests.get(source.url)
    soup = BeautifulSoup(url.content, "html.parser")
    length = source.items
    items = soup.find_all('item')[:length]
    contents = soup.find_all('content:encoded')[:length]
    covers = soup.find_all('media:content')[:length]

    for i in range(length-1, -1, -1):
        title = items[i].title.text
        body = contents[i].text
        try:
            cover = covers[i]['url']
        except:
            cover = ""
        category = Category.objects.get(pk=source.category.id)
        if not Post.objects.filter(title=title).exists():
            Post.objects.create(title=title,
                                body=str(body),
                                cover=str(cover),
                                category=category)
    return redirect("news:autoblogging")
