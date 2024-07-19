from django.contrib import admin
from django.urls import path, include

from account.urls import urlpatterns as account_urls
from app.urls import urlpatterns as app_urls
from utils.urls import urlpatterns as utils_urls

from .yasg import schema_view

from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(account_urls)),
    path('utils/', include(utils_urls)),
    path('app/', include(app_urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(
#             r'^api/media/(?P<path>.*)$',
#             serve,
#             {'document_root': settings.MEDIA_ROOT}
#         ),
#         re_path(
#             r'^api/static/(?P<path>.*)$',
#             serve,
#             {'document_root': settings.STATIC_ROOT}
#         ),
#     ]
# else:
#     urlpatterns += [
#         re_path(
#             r'^api/media/(?P<path>.*)$',
#             serve,
#             {'document_root': settings.MEDIA_ROOT}
#         ),
#         re_path(
#             r'^api/static/(?P<path>.*)$',
#             serve,
#             {'document_root': settings.STATIC_ROOT}
#         ),
#     ]
