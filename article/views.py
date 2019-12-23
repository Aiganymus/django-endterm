from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from article.models import Article
from article.serializers import ArticleShortSerializer, ArticleFullSerializer
from utils.permissions import CreatorPermission


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, CreatorPermission)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleShortSerializer
        return ArticleFullSerializer

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

