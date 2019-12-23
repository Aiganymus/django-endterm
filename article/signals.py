from django.db.models.signals import post_delete
from django.dispatch import receiver

from article.models import ArticleImage
from utils.upload import delete_image


@receiver(post_delete, sender=ArticleImage)
def delete_avatar(sender, instance, **kwargs):
    if instance.image:
        try:
            delete_image(instance.image)
        except Exception:
            pass
