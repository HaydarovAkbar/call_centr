from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User, Permission, Group


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["is_active"] = self.user.is_active
        attrs["full_name"] = self.user.first_name + " " + self.user.last_name
        attrs['is_staff'] = self.user.is_staff
        attrs['is_superuser'] = self.user.is_superuser
        attrs["groups"] = [group.name for group in self.user.groups.all()]
        # attrs["permissions"] = [permission.codename for permission in self.user.groups.first().permissions.all()]
        return attrs

    class Meta:
        model = User
        fields = ['username', 'password']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']