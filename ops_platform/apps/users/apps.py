from django.apps import AppConfig




class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ops_platform.apps.users'
    verbose_name = "用户信息"
    verbose_name_plural = "用户信息"
