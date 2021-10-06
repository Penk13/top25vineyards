from django.urls import path

from .views import (mainpage, footerpage, searchpage, page, travel_news_page)

app_name = 'pages_app'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('<slug:slug>/', footerpage, name='footerpage'),
    path('page/search/', searchpage, name='searchpage'),
    path('page/global-travel-news/', travel_news_page, name='newspage'),
    path('page/<slug:slug>/', page, name='page'),
]
