from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

from .models import Application 


@receiver(post_save, sender=Application)
def application_created(sender, instance, created, **kwargs):

    if created:
        print("Yangi ariza yaratildi:", instance.id)
    else:
        print("Ariza yangilandi:", instance.id)

@receiver(post_delete, sender=Application)
def application_deleted(sender, instance, **kwargs):
    
    print("Ariza o'chirildi:", instance.id)
