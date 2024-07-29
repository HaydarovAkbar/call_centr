from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from .serializers import AppealSerializer, AppealCreateSerializer
from .models import Appeal
from .permissions import IsCallCenter
from .pagination import TenPagination
from .filters import AppealDatetimeFilters


class AppealListView(ListAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    filter_backends = [DjangoFilterBackend, AppealDatetimeFilters]
    filterset_fields = ['user', 'phone_number', 'district', 'region']
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', ]
    pagination_class = TenPagination


class AppealCreateView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealCreateSerializer
    permission_classes = [IsCallCenter, IsAuthenticated]
    http_method_names = ['post', ]

    # parser_classes = [MultiPartParser, FormParser, FileUploadParser]  # JSONParser

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data['user'] = user.id
        return super().create(request, *args, **kwargs)


class AppealRetrieveView(RetrieveAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    # permission_classes = [IsAuthenticated, IsCallCenter]
    http_method_names = ['get', ]


class AppealUpdateView(UpdateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealCreateSerializer
    # permission_classes = [IsAuthenticated, IsCallCenter]
    http_method_names = ['patch', ]
