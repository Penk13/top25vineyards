from django.urls import path

from .views import (vineyard_detail, vineyard_region, rr_form, edit_vineyard)

app_name = 'vineyards'
urlpatterns = [
    path('edit-a-vineyard/<str:vineyard>/', edit_vineyard, name="edit-vineyard"),
    path('<str:parent>/<str:region>/vineyard/<slug:slug>/review/',
         rr_form, name="detail-form"),
    path('<str:region>/vineyard/<slug:slug>/review/',
         rr_form, name="detail-without-parent-form"),
    path('<str:parent>/<str:region>/vineyard/<slug:slug>/',
         vineyard_detail, name="detail"),
    path('<str:region>/vineyard/<slug:slug>/',
         vineyard_detail, name="detail-without-parent"),
    path('<str:parent>/<str:region>/',
         vineyard_region, name="region"),
    path('<str:region>/',
         vineyard_region, name="region-without-parent"),
]
