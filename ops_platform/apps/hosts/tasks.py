import os

from celery import shared_task

from ops_platform.utils.ssh import SSH
from .models import Hosts
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import logging

logger = logging.getLogger("celery")


@shared_task(bind=True, max_retries=3, soft_time_limit=10)
def check_host_status(host_id):
    obj = Hosts.objects.get(id=host_id)
    host_id = obj.id
    host_name = obj.host_name
    port = obj.port
    username = obj.username
    status = SSH(host_name, port, username).ping() or False
    channel_layer = get_channel_layer()
    logger.error(f"检查{host_name}是否在线")
    async_to_sync(channel_layer.group_send)(
        "host_status",  # 频道组名
        {
            "type": "host_status_update",  # 对应消费者方法名
            "data": {
                "host_id": host_id,
                "status": status,
                "timestamp": os.times()
            }
        }
    )


@shared_task(bind=True, max_retries=3, soft_time_limit=10)
def check_all_hosts():
    logger.info(f"检查所有是否在线")
    for host in Hosts.objects.all():
        check_host_status.delay(host)
