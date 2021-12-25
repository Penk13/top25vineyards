from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
from vineyards.models import Vineyard, VineyardUser


@receiver(post_save, sender=VineyardUser)
def from_admin_email(sender, instance, **kwargs):
    if instance.vineyard.display is False and instance.vineyard.send_email is True:
        subject = "Thank you for your submitting the vineyard"
        body = "Admin will first review your vineyard before it is displayed"
        # Email sent to user
        send_mail(subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [instance.email1])
        print("FROM ADMIN EMAIL")


@receiver(post_save, sender=VineyardUser)
def from_user_email(sender, instance, **kwargs):
    if instance.vineyard.display is False and instance.vineyard.send_email is True:
        subject = "Vineyard from User"
        body = instance.vineyard.name + '\n\n' + instance.name + '\n\n' + instance.email1
        # Email sent to admin
        send_mail(subject,
                body,
                '',
                [settings.DEFAULT_FROM_EMAIL])
        print("FROM USER EMAIL")


@receiver(post_save, sender=Vineyard)
def vineyard_go_live(sender, instance, **kwargs):
    try:
        vuser = VineyardUser.objects.get(vineyard=instance.id)
        if instance.display is True and instance.vineyard.send_email is True:
            domain = Site.objects.get_current().domain  # https://www.top25vineyards.com/
            path = instance.get_absolute_url()  # link to the vineyard (for example : vineyards/france/bordeaux/vineyard/chateau-monlot/)

            subject = "Your vineyard is now live"
            body = 'https://' + domain + path

            send_mail(subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [vuser.email1])
            print("VINEYARD GO LIVE")
    except:
        pass
