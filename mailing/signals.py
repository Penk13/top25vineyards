from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactEntry, Subscriber


@receiver(post_save, sender=ContactEntry)
def from_user(sender, instance, **kwargs):
    # Email sent to admin
    send_mail(instance.subject,
              instance.message + "\n\n" + "From: " + instance.name + "\nEmail: " + instance.email,
              '',
              [settings.DEFAULT_FROM_EMAIL])


@receiver(post_save, sender=Subscriber)
def from_user(sender, instance, **kwargs):
    # Email sent to admin
    send_mail("Subscriber",
              "From: " + instance.name + "\nEmail: " + instance.email + "\nCountry: " + instance.country,
              '',
              [settings.DEFAULT_FROM_EMAIL])


@receiver(post_save, sender=Subscriber)
def from_admin(sender, instance, **kwargs):
    # Email sent to user
    send_mail("Confirmation Subscription",
              "Thanks for subscribing to our newsletter!",
              settings.DEFAULT_FROM_EMAIL,
              [instance.email])
