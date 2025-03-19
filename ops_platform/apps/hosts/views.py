# Create your views here.
from rest_framework.renderers import HTMLFormRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class HostCategoryApiViews(ModelViewSet):
    queryset = models.HostsCategory.objects.filter(is_deleted=False).order_by("-id").all()
    serializer_class = serializers.HostCategorySerializers
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


class HostApiViews(ModelViewSet):
    queryset = models.Hosts.objects.filter(is_deleted=False).order_by("-id").all()
    serializer_class = serializers.HostsSerializers
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [HTMLFormRenderer, BrowsableAPIRenderer]
