from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView


# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter


class LoginApiView(TokenObtainPairView):
    """The class is responsible for LogIn functionality and Tokenaization"""
    serializer_class = serializers.LogInSerializer
