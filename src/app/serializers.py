from rest_framework import serializers

from .models import Appeal, FAQ
from django.contrib.auth.models import User


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['district_title'] = instance.district.title if instance.district else None
        response['region_title'] = instance.region.title if instance.region else None
        response['user_title'] = (instance.user.first_name + ' ' + instance.user.last_name) if instance.user else None
        response['voice'] = instance.get_voice_url()
        return response


class AppealCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ('app_name', 'app_datetime', 'result', 'text', 'done', 'phone_number', 'district', 'region', 'voice',
                  'is_active', 'is_resolved', 'created_at', 'user')


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'title', 'question')