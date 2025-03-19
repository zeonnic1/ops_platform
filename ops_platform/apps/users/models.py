from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号码")
    avatar = models.ImageField(upload_to="avartar", verbose_name="用户头像", null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
        db_table = "uric_user"
