"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.http import Http404
from django.urls import path, include
from multiurl import ContinueResolving, multiurl

from accounts.views import profile
from news.views import news_detail, autoblogging, pull_feeds
from pages_app.views import mainpage, footerpage, searchpage, page, newspage, articlespage
from vineyards.views import vineyard_detail, vineyard_region, rr_form, edit_vineyard

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # accounts
    path('', include('allauth.urls')),
    path('profile/', profile, name='profile'),

    # news
    path('news/autoblogging/', autoblogging, name='news-autoblogging'),
    path('pull/<int:pk>/', pull_feeds, name='news-pull'),

    # pages_app
    path('', mainpage, name='mainpage'),
    path('search/', searchpage, name='searchpage'),
    multiurl(
        path('<slug:slug>/', footerpage, name='footerpage'),
        path('<str:region>/', vineyard_region, name="region-without-parent"),
        path('<slug:slug>/', newspage, name='newspage'),
        catch = (Http404, ContinueResolving)
    ),
    path('explore/<slug:slug>/', page, name='page'),
    path('article/<slug:slug>/', articlespage, name='articlespage'),

    # vineyards
    path('edit-a-vineyard/<str:vineyard>/', edit_vineyard, name="edit-vineyard"),
    path('review/<str:parent>/<str:region>/vineyard/<slug:slug>/',
         rr_form, name="vineyard-review"),
    path('review/<str:region>/vineyard/<slug:slug>/',
         rr_form, name="vineyard-without-parent-review"),
    path('<str:parent>/<str:region>/vineyard/<slug:slug>/',
         vineyard_detail, name="vineyard-detail"),
    path('<str:region>/vineyard/<slug:slug>/',
         vineyard_detail, name="vineyard-detail-without-parent"),

    multiurl(
        path('<str:parent>/<str:region>/',
            vineyard_region, name="region"),
        path('<slug:category>/<slug:news>/', news_detail, name='news-detail'),
        catch = (Http404, ContinueResolving)
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
