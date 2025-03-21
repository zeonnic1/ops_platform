from django.db import models

from ops_platform.apps.users.models import Users


# Create your models here.

class BaseModel(models.Model):
    name = models.CharField(max_length=500, default="", null=True, blank=True, verbose_name="名称/标题")
    is_show = models.BooleanField(default=True, verbose_name='是否显示')
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    desciption = models.CharField(max_length=500, default="", null=True, blank=True, verbose_name="描述信息")

    class Meta:
        abstract = True


class HostsCategory(BaseModel):
    class Meta:
        db_table = 'uric_hosts_category'
        verbose_name = "主机类别"
        verbose_name_plural = "主机类别"

    def __str__(self):
        return self.name


class Hosts(BaseModel):
    category = models.ForeignKey("HostsCategory", on_delete=models.DO_NOTHING, related_name="hc", null=True, blank=True,
                                 verbose_name="主机类别")
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name="主机名称")
    host_name = models.CharField(max_length=20, blank=True, null=True, verbose_name="连接地址")
    port = models.IntegerField(blank=True, null=True, verbose_name="端口")
    username = models.CharField(max_length=20, blank=True, null=True, verbose_name="用户名")
    users = models.ManyToManyField(Users)

    class Meta:
        db_table = "uric_hosts"
        verbose_name: "主机信息"
        verbose_name_plural: "主机信息"

    def __str__(self):
        return f"{self.name} {self.ip_addr}:{self.port}"
