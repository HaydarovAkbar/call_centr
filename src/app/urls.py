from .views import AppealListView, AppealCreateView

from django.urls import path

urlpatterns = [
    path('appeals/', AppealListView.as_view(), name='appeal-list'),
    path('appeals/create/', AppealCreateView.as_view(), name='appeal-create'),
]
