from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomUserCreate

from rest_framework.authtoken.views import ObtainAuthToken
from .views import WorkViewSet, ArtistViewSet


router = DefaultRouter()
router.register('works', WorkViewSet, basename='work')
router.register('artists', ArtistViewSet, basename='artist')

urlpatterns = [
    path('api/register/', CustomUserCreate.as_view(), name='user_register'),
    path('api/', include(router.urls)),
    path('api/token/', ObtainAuthToken.as_view(), name='token_obtain'),
]