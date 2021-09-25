from django.urls import path

from .views import (mainpage, footerpage)

app_name = 'pages_app'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('<slug:slug>/', footerpage, name='footerpage'),
]
