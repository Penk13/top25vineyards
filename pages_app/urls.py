from django.urls import path

from .views import (mainpage, footerpage, searchpage, page, newspage)

app_name = 'pages_app'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('<slug:slug>/', footerpage, name='footerpage'),
    path('page/search/', searchpage, name='searchpage'),
    path('news-list/<slug:slug>/', newspage, name='newspage'),
    path('page/<slug:slug>/', page, name='page'),
]
