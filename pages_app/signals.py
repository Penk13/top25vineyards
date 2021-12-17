from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
from vineyards.models import Vineyard, VineyardUser


@receiver(post_save, sender=VineyardUser)
def from_admin_email(sender, instance, **kwargs):
    if instance.vineyard.display is False:
        subject = "Thank you for your submitting the vineyard"
        body = "Admin will first review your vineyard before it is displayed"
    # Email sent to user
    send_mail(subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email1])


@receiver(post_save, sender=VineyardUser)
def from_user_email(sender, instance, **kwargs):
    if instance.vineyard.display is False:
        # Email sent to admin
        send_mail("Vineyard from User",
                instance.vineyard.name + '\n\n' +
                instance.name + '\n\n' +
                instance.email1,
                '',
                [settings.DEFAULT_FROM_EMAIL])


@receiver(post_save, sender=Vineyard)
def vineyard_go_live(sender, instance, **kwargs):
    try:
        vuser = VineyardUser.objects.get(vineyard=instance.id)
        if instance.display is True:
            domain = Site.objects.get_current().domain
            path = instance.get_absolute_url()
            subject = "Your vineyard is now live"
            body = 'https://' + domain + path
            send_mail(subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [vuser.email1])
    except:
        pass