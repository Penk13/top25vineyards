from django.urls import path

from .views import (news_detail)

app_name = 'news'
urlpatterns = [
    path('<slug:slug>/', news_detail, name='detail'),
]
