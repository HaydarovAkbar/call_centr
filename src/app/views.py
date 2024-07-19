from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.response import Response

from .serializers import AppealSerializer, AppealCreateSerializer
from .models import Appeal
from .permissions import IsCallCenter


class AppealListView(ListAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'phone_number', 'district', 'region']
    # permission_classes = [IsAuthenticated, IsCallCenter]
    http_method_names = ['get', ]


class AppealCreateView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealCreateSerializer
    # permission_classes = [IsAuthenticated, IsCallCenter]
    http_method_names = ['post', ]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]  # JSONParser

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            request.data['user'] = user.id
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=403)


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
