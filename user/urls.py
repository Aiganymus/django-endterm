from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

from user.views import RegisterUserAPIView, ProfileViewSet

urlpatterns = [
    path('login', obtain_jwt_token),
    path('register', RegisterUserAPIView.as_view())
]

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, basename='user')

urlpatterns += router.urls
