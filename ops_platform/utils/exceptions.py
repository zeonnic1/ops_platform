import logging

from rest_framework.views import exception_handler
from django.db import DatabaseError

from rest_framework import status
from rest_framework.response import Response

logger = logging.getLogger("django")


def custom_exception_handler(exc, content):
    response = exception_handler(exc, content)

    if response == None:
        views = content['view']
        if isinstance(exc,DatabaseError):
            logger.error(f"{views} {exc}")
            response = Response({"errormsg": "服务器错误"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
