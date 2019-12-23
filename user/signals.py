from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from user.models import MainUser, Profile
from utils.upload import delete_image


@receiver(post_save, sender=MainUser)
def create_profile(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_delete, sender=Profile)
def delete_avatar(sender, instance, **kwargs):
    if instance.avatar:
        delete_image(instance.avatar)
