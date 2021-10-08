from django.urls import path

from .views import (news_detail)

app_name = 'news'
urlpatterns = [
    path('<slug:category>/<slug:news>/', news_detail, name='detail'),
]
