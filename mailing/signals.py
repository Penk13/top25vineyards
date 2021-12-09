from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactEntry, Subscriber


@receiver(post_save, sender=ContactEntry)
def contact_from_user(sender, instance, **kwargs):
    # Email sent to admin
    send_mail(instance.subject,
              instance.message + "\n\n" + "From: " + instance.name,
              '',
              [settings.DEFAULT_FROM_EMAIL])


@receiver(post_save, sender=Subscriber)
def contact_from_user(sender, instance, **kwargs):
    # Email sent to admin
    send_mail("Subscriber",
              "From: " + instance.email,
              '',
              [settings.DEFAULT_FROM_EMAIL])
