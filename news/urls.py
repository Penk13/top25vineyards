from django.urls import path

from .views import (news_detail, autoblogging, pull_feeds)

app_name = 'news'
urlpatterns = [
    path('autoblogging/', autoblogging, name='autoblogging'),
    path('pull/<int:pk>/', pull_feeds, name='pull'),
    path('<slug:category>/<slug:news>/', news_detail, name='detail'),
]
