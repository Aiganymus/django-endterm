import os

from django.core.exceptions import ValidationError

from utils.constants import IMAGE_ALLOWED_EXTS


def image_size(value):
    if value.size > 2*1024*1024:
        raise ValidationError('image size too large (> 2mb)!')


def image_extension(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in IMAGE_ALLOWED_EXTS:
        raise ValidationError(f'extension not allowed, allowed ({IMAGE_ALLOWED_EXTS}')
