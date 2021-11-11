from django.urls import path

from .views import profile, account_login_view

app_name = 'accounts'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', view=account_login_view, name='account_login'),
]
