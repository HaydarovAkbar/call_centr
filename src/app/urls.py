from .views import AppealListView, AppealCreateView, AppealRetrieveView, AppealUpdateView

from django.urls import path

urlpatterns = [
    path('appeals/', AppealListView.as_view(), name='appeal-list'),
    path('appeals/create/', AppealCreateView.as_view(), name='appeal-create'),
    path('appeals/<int:pk>/', AppealRetrieveView.as_view(), name='appeal-detail'),
    path('appeals/<int:pk>/update/', AppealUpdateView.as_view(), name='appeal-update'),
]
