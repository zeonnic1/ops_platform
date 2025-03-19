import logging

from django.utils.deprecation import MiddlewareMixin
import time

logger = logging.getLogger("django_request")


class LogMIDDLEWARE(MiddlewareMixin):

    # def __init__(self, get_response):
    #     super().__init__(get_response)
    #     self.start_time = None

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        cost_time = time.time() - request.start_time
        if cost_time > 0.1 or True:
            logger.warning(f"请求路径: {request.path} 请求耗时：{cost_time}")
        return response
