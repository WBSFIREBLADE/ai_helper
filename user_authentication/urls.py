from django.urls import path
from .views import RegisterAPIView, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Login → access + refresh token
    TokenRefreshView,     # Refresh access token
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]   