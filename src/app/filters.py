from rest_framework.filters import BaseFilterBackend


class AppealDatetimeFilters(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        date_from = request.query_params.get('date_from', False)
        date_to = request.query_params.get('date_to', False)

        if date_to and date_from:
            return queryset.filter(app_datetime__range=[date_from, date_to])
        elif date_to:
            return queryset.filter(app_datetime__lte=date_to)
        elif date_from:
            return queryset.filter(app_datetime__gte=date_from)
        return queryset
