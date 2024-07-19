from django.contrib import admin
from django.urls import path, include

from account.urls import urlpatterns as account_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(account_urls)),
]
