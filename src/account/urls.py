from django.urls import path

from .views import LoginApiView, UserListView  # , FacebookLogin

urlpatterns = [
    path('login/', LoginApiView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='users_list'),
    # path('login/facebook/', FacebookLogin.as_view(), name='fb_login'),
]
