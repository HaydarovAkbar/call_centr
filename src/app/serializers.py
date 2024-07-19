from rest_framework import serializers

from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'


class AppealCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ('app_name', 'app_datetime', 'result', 'text', 'done', 'phone_number', 'district', 'region', 'voice',
                  'is_active', 'is_resolved', 'created_at')
