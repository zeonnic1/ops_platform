from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import os
from django.core.asgi import get_asgi_application
from ops_platform.apps.hosts import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ops_platform.settings.dev')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # 处理 HTTP 请求
    "websocket": AuthMiddlewareStack(  # 支持 Session 认证
        URLRouter(
            routing.websocket_urlpatterns  # 指向路由配置
        )
    ),
})
