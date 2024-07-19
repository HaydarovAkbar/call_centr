from rest_framework import serializers

from .models import Region, District


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'title', 'attr')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'title', 'region', 'get_region_name')