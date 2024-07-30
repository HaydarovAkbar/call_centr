from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListAPIView
from . import serializers
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView


# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter


class LoginApiView(TokenObtainPairView):
    """The class is responsible for LogIn functionality and Tokenaization"""
    serializer_class = serializers.LogInSerializer


class UserListView(ListAPIView):
    """The class is responsible for listing all users"""
    queryset = serializers.User.objects.all()
    serializer_class = serializers.UserSerializers
    http_method_names = ['get', ]

    def get_queryset(self):
        return self.queryset.filter(groups__name='call_center')