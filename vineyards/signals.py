from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from .models import ReviewAndRating, Comment, Vineyard
import datetime


@receiver(post_save, sender=Vineyard)
def from_user_vineyard(sender, instance, **kwargs):
    if instance.display is False and instance.send_email is True:
        subject = "Vineyard from User"
        body = instance.name + '\n\n' + instance.user.username + '\n\n' + instance.email1
        # Email sent to admin
        send_mail(subject,
                body,
                '',
                [settings.DEFAULT_FROM_EMAIL])


@receiver(post_save, sender=Vineyard)
def from_admin_vineyard(sender, instance, **kwargs):
    if instance.display is True and instance.send_email is True:
        domain = Site.objects.get_current().domain  # https://www.top25vineyards.com/
        path = instance.get_absolute_url()  # link to the vineyard (for example : vineyards/france/bordeaux/vineyard/chateau-monlot/)

        subject = "Your vineyard is now live"
        body = domain + path

        send_mail(subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [instance.email1])

    elif instance.display is False and instance.send_email is True:
        subject = "Thank you for your submitting the vineyard"
        body = "Admin will first review your vineyard before it is displayed"
        # Email sent to user
        send_mail(subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [instance.email1])


@receiver(post_save, sender=ReviewAndRating)
def from_admin_rr(sender, instance, **kwargs):
    if instance.approved is True:
        domain = Site.objects.get_current().domain
        path = instance.vineyard.get_absolute_url()
        subject = "Your review and rating are now live"
        body = render_to_string(
            'approval-email.html',
            {
                'username': instance.user.username,
                'vineyard_url': 'https://' + domain + path,
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
def from_user_rr(sender, instance, **kwargs):
    if instance.approved is False:
        # Email sent to admin
        send_mail("Review from User",
                  instance.vineyard.name + '\n\n' +
                  instance.title + '\n\n' +
                  instance.review,
                  '',
                  [settings.DEFAULT_FROM_EMAIL])


@receiver(post_save, sender=Comment)
def from_admin_comment(sender, instance, **kwargs):
    rr = instance.rr
    if instance.approved is True:
        domain = Site.objects.get_current().domain
        path = rr.vineyard.get_absolute_url()
        # Email sent to admin
        send_mail("Your comment is now live",
                  'https://' + domain + path + '\n\n',
                   settings.DEFAULT_FROM_EMAIL,
                   [instance.user.email])
    else:
        # Email sent to user
        send_mail("Thank you for your comment",
                   instance.title,
                   settings.DEFAULT_FROM_EMAIL,
                   [instance.user.email])


@receiver(post_save, sender=Comment)
def from_user_comment(sender, instance, **kwargs):
    rr = instance.rr
    if instance.approved is False:
        # Email sent to admin
        send_mail("Comment from User",
                  rr.vineyard.name + '\n\n' +
                  instance.title + '\n\n' +
                  instance.body,
                  '',
                  [settings.DEFAULT_FROM_EMAIL])
