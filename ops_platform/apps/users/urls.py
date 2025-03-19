from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [

    path('login', TokenObtainPairView.as_view()),
    path('jwt/refresh', TokenRefreshView.as_view()),
    path('jwt/verify', TokenVerifyView.as_view()),
]
