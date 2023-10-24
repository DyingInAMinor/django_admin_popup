import time

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyCustomModel


@receiver(post_save, sender=MyCustomModel)
def your_custom_signal_handler(sender, instance, created, **kwargs):
    print("Hehe")
    time.sleep(10)
