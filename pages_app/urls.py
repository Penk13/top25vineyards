from django.urls import path

from .views import (mainpage, footerpage, searchpage, page)

app_name = 'pages_app'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('<slug:slug>/', footerpage, name='footerpage'),
    path('page/search/', searchpage, name='searchpage'),
    path('page/<slug:slug>', page, name='page'),
]
