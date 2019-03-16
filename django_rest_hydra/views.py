import json
import pdb

from django.http import JsonResponse
from rest_framework import status

from rest_framework.views import APIView
from django.conf import settings


class TestView(APIView):

    def get(self, request):
        return JsonResponse(settings.REST_HYDRA, status=status.HTTP_200_OK, safe=False)
