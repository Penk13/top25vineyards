from django.urls import path

from .views import (vineyard_detail)

app_name = 'vineyards'
urlpatterns = [
    path('detail/<int:pk>/', vineyard_detail, name="detail")
]
