from .views import AppealListView, AppealCreateView, AppealRetrieveView, AppealUpdateView, ImportAppealView, \
    FAQListView, StatsAppealView, ChangeAppealStatusView, StatusListView, AnswersListView

from django.urls import path

urlpatterns = [
    path('appeals/', AppealListView.as_view(), name='appeal-list'),
    path('appeals/create/', AppealCreateView.as_view(), name='appeal-create'),
    path('appeals/<int:pk>/', AppealRetrieveView.as_view(), name='appeal-detail'),
    path('appeals/<int:pk>/update/', AppealUpdateView.as_view(), name='appeal-update'),
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('appeals/import/', ImportAppealView.as_view(), name='appeal-import'),
    path('stats/', StatsAppealView.as_view(), name='stats'),
    path('answers/', AnswersListView.as_view(), name='answers'),
    path('status/', StatusListView.as_view(), name='status-list'),
    path('status/<int:pk>/', ChangeAppealStatusView.as_view(), name='status-change'),
]
