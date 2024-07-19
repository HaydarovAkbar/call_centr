from .views import RegionListView, DistrictListView
from django.urls import path

urlpatterns = [
    path('regions/', RegionListView.as_view(), name='region-list'),
    path('districts/', DistrictListView.as_view(), name='district-list'),
]
