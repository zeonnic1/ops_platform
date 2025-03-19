"""
URL configuration for ops_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# from apps.users import views as users_views

# urlpatterns = [
#     path('login/', users_views.login_get, name='login'),
#     path('login_post/', users_views.login_post, name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('register/', users_views.register, name='register'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('', include('apps.blog.urls'), name="blog"),
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('users/', include('users.urls')),
    path('hosts/', include('hosts.urls')),
]
