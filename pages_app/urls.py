from django.urls import path

from .views import (mainpage, contact_us, about_us, terms_of_service,
                    privacy_statement, newsletter, advertise_with_us, help_or_faq, site_map)

app_name = 'pages_app'
urlpatterns = [
    path('', mainpage, name='mainpage'),

    path('contact-us/', contact_us, name='contact_us'),
    path('about-us/', about_us, name='about_us'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
    path('privacy-statement/', privacy_statement, name='privacy_statement'),

    path('newsletter/', newsletter, name='newsletter'),
    path('advertise-with-us/', advertise_with_us, name='advertise_with_us'),
    path('help-or-faq/', help_or_faq, name='help_or_faq'),
    path('site-map/', site_map, name='site_map'),
]
