from django.urls import path

from .views import (mainpage, footerpage, searchpage)

app_name = 'pages_app'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('<slug:slug>/', footerpage, name='footerpage'),
    path('page/search/', searchpage, name='searchpage'),
]
