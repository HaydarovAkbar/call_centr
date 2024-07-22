from django.urls import path


from .views import LoginApiView # , FacebookLogin

urlpatterns = [
    path('login/', LoginApiView.as_view(), name='login'),
    # path('login/facebook/', FacebookLogin.as_view(), name='fb_login'),
]
