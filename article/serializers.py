from django.db import transaction
from rest_framework import serializers

from article.models import Article, ArticleImage
from user.serializers import UserSerializer


class ArticleShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'description', 'price', 'city', 'category', 'color')

    def validate_color(self, value):
        print(value)
        if 1 > value > 3:
            raise serializers.ValidationError('color must be 1, 2, 3')
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('price must be positive')
        return value


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('image', )


class ArticleFullSerializer(ArticleShortSerializer):
    images_uploaded = serializers.ListField(
        child=serializers.FileField(), required=False, write_only=True
    )
    images = ArticleImageSerializer(many=True, read_only=True)
    creator = UserSerializer(read_only=True)

    class Meta(ArticleShortSerializer.Meta):
        fields = ArticleShortSerializer.Meta.fields + ('creator', 'images', 'images_uploaded')

    def create(self, validated_data):
        with transaction.atomic():
            images = []
            if 'images_uploaded' in validated_data:
                images = validated_data.pop('images_uploaded')
            article = Article(**validated_data)
            article.save()
            ArticleImage.objects.bulk_create([ArticleImage(article=article, image=img) for img in images])
            return article
