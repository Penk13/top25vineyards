import requests
import os
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.core import files
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
            content = contents[i].text
            title = items[i].title.text
            body = content[content.find('<p>'):]

            category = Category.objects.get(pk=source.category.id)
            if not Post.objects.filter(title=title).exists():
                post = Post(title=title,
                            body=body,
                            category=category)

                link = content[content.find('src=')+5:content.find('alt')-2]
                img_data = requests.get(link).content
                with open('temp_image.jpg', 'wb') as handler:
                    handler.write(img_data)
                with open('temp_image.jpg', 'rb') as handler:
                    file_name = link.split("/")[-1]
                    post.cover.save(file_name, files.File(handler))
            os.remove("temp_image.jpg")
        return redirect("news:autoblogging")
    else:
        return HttpResponse("Sorry you are not allowed to access this page")
