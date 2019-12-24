# noinspection PyUnresolvedReferences
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .admin_request_views import AdminRequestView

from .models import Requests, Categories
# noinspection PyUnresolvedReferences
from .request_serializer import RequestSerializer

class RequestView(APIView):

    def get(self, request):
        return AdminRequestView.get(self, request)