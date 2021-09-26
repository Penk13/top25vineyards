from django.urls import path

from .views import (vineyard_detail, vineyard_region)

app_name = 'vineyards'
urlpatterns = [
    path('detail/<int:pk>/', vineyard_detail, name="detail"),
    path('<slug:slug>/', vineyard_region, name="region"),
]
