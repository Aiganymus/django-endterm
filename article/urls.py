from django.urls import path
from rest_framework import routers

from article.views import ArticleViewSet, ArticleFavoriteAPIView

urlpatterns = [
    path('articles/favorite/', ArticleFavoriteAPIView.as_view())
]

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns += router.urls
