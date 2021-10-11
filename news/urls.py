from django.urls import path

from .views import (news_detail, autoblogging)

app_name = 'news'
urlpatterns = [
    path('autoblogging/', autoblogging, name='autoblogging'),
    path('<slug:category>/<slug:news>/', news_detail, name='detail'),
]
