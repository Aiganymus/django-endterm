import os
import shutil


def avatar_path(instance, filename):
    pk = instance.user.id
    return f'avatars/{pk}-{filename}'


def article_image(instance, filename):
    pk = instance.article.id
    return f'article/{pk}/{filename}'


def delete_image(media):
    path = os.path.abspath(os.path.join(media.path, '..'))
    shutil.rmtree(path)

