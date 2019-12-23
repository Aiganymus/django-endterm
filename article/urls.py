from rest_framework import routers

from article.views import ArticleViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns = router.urls
