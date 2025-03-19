from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import HostApiViews, HostCategoryApiViews

router = DefaultRouter()

router.register('host_category', HostCategoryApiViews, basename="category")
router.register('', HostApiViews, basename="hosts")

urlpatterns = [
    # path('',HostApiViews.as_view(actions={'get': 'list', 'post': 'create'}))
]
urlpatterns += router.urls
