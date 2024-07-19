from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers


class LoginApiView(TokenObtainPairView):
    """The class is responsible for LogIn functionality and Tokenaization"""
    serializer_class = serializers.LogInSerializer
