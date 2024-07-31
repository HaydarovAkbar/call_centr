from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.response import Response
import openpyxl as px
from django.http import FileResponse
import os
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from .serializers import AppealSerializer, AppealCreateSerializer, FAQSerializer
from .models import Appeal, FAQ
from .permissions import IsCallCenter
from .pagination import TenPagination
from .filters import AppealDatetimeFilters


class AppealListView(ListAPIView):
    queryset = Appeal.objects.all().order_by('-id')
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

    parser_classes = [MultiPartParser, FormParser, FileUploadParser]  # JSONParser

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


class FAQListView(ListAPIView):
    queryset = FAQ.objects.all().order_by('order')
    serializer_class = FAQSerializer
    http_method_names = ['get', ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'question']


class ImportAppealView(ListAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealCreateSerializer
    # permission_classes = [IsCallCenter, IsAuthenticated]
    http_method_names = ['get', ]
    filter_backends = [DjangoFilterBackend, AppealDatetimeFilters]
    filterset_fields = ['user', 'phone_number', 'district', 'region']

    def list(self, request, *args, **kwargs):
        filter_queryset = self.filter_queryset(self.get_queryset()).order_by('-id')
        excel_name = 'report.xlsx'
        excel_path = os.path.join(settings.STATIC_ROOT, excel_name)
        book = px.load_workbook(excel_path)
        wb = book.get_sheet_by_name('book')
        # wb.cell(3, 10,
        #         f'{now().date().year} yil {now().date().day} may soat {now().hour}:{now().strftime("%M")} holatiga')
        row, count = 4, 1
        for query in filter_queryset:
            wb.cell(row, 2, str(count))
            wb.cell(row, 3, query.region.title if query.region else None)
            wb.cell(row, 4, query.district.title if query.district else None)
            wb.cell(row, 5, query.app_name)
            wb.cell(row, 6, query.phone_number)
            wb.cell(row, 7, (query.user.first_name + ' ' + query.user.last_name) if query.user else None)
            wb.cell(row, 8, query.app_datetime.strftime('%Y-%m-%d %H:%M:%S'))
            wb.cell(row, 9, query.get_voice_url() if query.voice else None)
            row += 1
            count += 1
        book.save(f"static\data.xlsx")
        return FileResponse(open('static\data.xlsx', 'rb'))
