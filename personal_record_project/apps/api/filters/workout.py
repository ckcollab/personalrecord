from rest_framework import filters
import django_filters

from personal_record_project.apps.workout.models import Set


class BodyweightFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        bodyweight = request.QUERY_PARAMS.get('bodyweight', None)

        if bodyweight:
            bodyweight_range = bodyweight.split(",")

            if len(bodyweight_range) == 2:
                int_range = (int(bodyweight_range[0]), int(bodyweight_range[1]))
                queryset = queryset.filter(bodyweight__range=int_range)

        return queryset
