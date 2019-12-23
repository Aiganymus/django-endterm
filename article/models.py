from django.db import models

from user.models import MainUser
from utils.constants import COLOR_TYPES, GREEN
from utils.upload import article_image
from utils.validators import image_size, image_extension


class Article(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    color = models.PositiveSmallIntegerField(choices=COLOR_TYPES, default=GREEN)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='articles')


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to=article_image, validators=[image_size, image_extension])


class FavoriteArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favorite_by')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='favorites')
