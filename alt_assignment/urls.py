
from .views import UserViewSet, ProfileViewSet, TaskViewSet
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'profile', ProfileViewSet, basename='profile')



urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]