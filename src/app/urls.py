from .views import AppealListView, AppealCreateView, AppealRetrieveView, AppealUpdateView, ImportAppealView, FAQListView, StatsAppealView

from django.urls import path

urlpatterns = [
    path('appeals/', AppealListView.as_view(), name='appeal-list'),
    path('appeals/create/', AppealCreateView.as_view(), name='appeal-create'),
    path('appeals/<int:pk>/', AppealRetrieveView.as_view(), name='appeal-detail'),
    path('appeals/<int:pk>/update/', AppealUpdateView.as_view(), name='appeal-update'),
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('appeals/import/', ImportAppealView.as_view(), name='appeal-import'),
    path('stats/', StatsAppealView.as_view(), name='stats'),
]
