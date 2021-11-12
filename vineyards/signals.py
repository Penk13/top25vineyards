from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import ReviewAndRating
import datetime


@receiver(post_save, sender=ReviewAndRating)
def submission_email(sender, instance, **kwargs):
    body = render_to_string(
        'submission-email.html',
        {
            'username': instance.user.username,
            'title': instance.title,
            'date_created': datetime.datetime.now(),
            'email': settings.DEFAULT_FROM_EMAIL
        })
    # Email sent to user
    send_mail("Thank you for your rating and review",
              body,
              settings.DEFAULT_FROM_EMAIL,
              [instance.user.email])


@receiver(post_save, sender=ReviewAndRating)
def approval_email(sender, instance, **kwargs):
    # Email sent to admin
    send_mail("Review from User",
              instance.title + '\n\n' +
              instance.review,
              instance.user.email,
              [settings.DEFAULT_FROM_EMAIL])
