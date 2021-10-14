import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.core import files
from io import BytesIO
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Autoblogging, Category


def news_detail(request, category, news):
    news = get_object_or_404(Post, slug=news)
    context = {"news": news}
    return render(request, "news/news.html", context)


def autoblogging(request):
    if request.user.is_superuser:
        sources = Autoblogging.objects.all()
        context = {"sources": sources}
        return render(request, "news/autoblogging.html", context)
    else:
        return HttpResponse("Sorry you are not allowed to access this page")


def pull_feeds(request, pk):
    if request.user.is_superuser:
        source = Autoblogging.objects.get(pk=pk)

        url = requests.get(source.url)
        soup = BeautifulSoup(url.content, "html.parser")
        length = source.items
        items = soup.find_all('item')[:length]
        contents = soup.find_all('content:encoded')[:length]

        for i in range(length-1, -1, -1):
            title = items[i].title.text
            body = contents[i].text
            # Grab first pharagraph for body on list
            body_on_list = body[body.find(
                '/ TRAVELINDEX /')+15:body.find('/ TRAVELINDEX /')+215]

            link = body[body.find('src=')+5:body.find('alt')-2]
            resp = requests.get(link)
            fp = BytesIO()
            fp.write(resp.content)
            file_name = link.split("/")[-1]

            category = Category.objects.get(pk=source.category.id)
            if not Post.objects.filter(title=title).exists():
                post = Post(title=title,
                            body=str(body),
                            body_on_list=body_on_list,
                            category=category)
                post.cover.save(file_name, files.File(fp))
        return redirect("news:autoblogging")
    else:
        return HttpResponse("Sorry you are not allowed to access this page")
