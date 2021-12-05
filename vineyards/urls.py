from django.urls import path

from .views import (vineyard_detail, vineyard_region, rr_form)

app_name = 'vineyards'
urlpatterns = [
    path('<str:parent>/<str:region>/<slug:slug>/vineyard/review/',
         rr_form, name="detail-form"),
    path('<str:region>/<slug:slug>/vineyard/review/',
         rr_form, name="detail-without-parent-form"),
    path('<str:parent>/<str:region>/<slug:slug>/vineyard/',
         vineyard_detail, name="detail"),
    path('<str:region>/<slug:slug>/vineyard/',
         vineyard_detail, name="detail-without-parent"),
    path('<str:parent>/<str:region>/',
         vineyard_region, name="region"),
    path('<str:region>/',
         vineyard_region, name="region-without-parent"),
]
