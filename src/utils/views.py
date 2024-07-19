from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RegionSerializer, DistrictSerializer

from .models import Region, District


class RegionListView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'attr']


class DistrictListView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'region']