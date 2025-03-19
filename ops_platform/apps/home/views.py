from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import DatabaseError
import logging

# Create your views here.
logger = logging.getLogger("django.request")

loggerd = logging.getLogger("django")


class TestView(APIView):
    def get(self, request):
        logger.debug("Test debug log")
        loggerd.info("Test info log")
        return Response({"message": "hello test"})
