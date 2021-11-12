from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from .models import ReviewAndRating
import datetime


@receiver(post_save, sender=ReviewAndRating)
def from_admin_email(sender, instance, **kwargs):
    if instance.approved is True:
        domain = Site.objects.get_current().domain
        path = instance.vineyard.get_absolute_url()
        subject = "Your review and rating are now live"
        body = render_to_string(
            'approval-email.html',
            {
                'username': instance.user.username,
                'vineyard_url': domain + path,
                'email': settings.DEFAULT_FROM_EMAIL
            })
    else:
        subject = "Thank you for your rating and review"
        body = render_to_string(
            'submission-email.html',
            {
                'username': instance.user.username,
                'title': instance.title,
                'date_created': datetime.datetime.now(),
                'email': settings.DEFAULT_FROM_EMAIL
            })
    # Email sent to user
    send_mail(subject,
              body,
              settings.DEFAULT_FROM_EMAIL,
              [instance.user.email])


@receiver(post_save, sender=ReviewAndRating)
def from_user_email(sender, instance, **kwargs):
    if instance.approved is False:
        # Email sent to admin
        send_mail("Review from User",
                  instance.title + '\n\n' +
                  instance.review,
                  instance.user.email,
                  [settings.DEFAULT_FROM_EMAIL])
