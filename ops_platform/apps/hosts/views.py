# Create your views here.
from rest_framework.renderers import HTMLFormRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
from .tasks import check_all_hosts, check_host_status


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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # 触发异步检查
    #     for host in queryset:
    #         check_host_status.delay(host.id)
    #     return queryset
    def list(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        check_all_hosts.delay()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return super().list(request, *args, **kwargs)

    # 可选：在 retrieve 时触发单机检查
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        check_host_status.delay(instance.id)  # 异步触发单机检查
        return super().retrieve(request, *args, **kwargs)
