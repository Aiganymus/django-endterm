from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from article.serializers import ArticleShortSerializer, ArticleFullSerializer, FavoriteArticleSerializer
from utils.permissions import CreatorPermission
import logging


logger = logging.getLogger(__name__)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, CreatorPermission)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleShortSerializer
        return ArticleFullSerializer

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class ArticleFavoriteAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = FavoriteArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            logger.info(f"user '{request.user.username}' liked article with id={request.data.get('article_id')}")
            return Response('ok')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        favorites = request.user.favorites.all()
        articles = Article.objects.filter(id__in=favorites.values_list('article_id'))
        serializer = ArticleShortSerializer(articles, many=True)
        return Response(serializer.data)
