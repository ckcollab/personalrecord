from django.shortcuts import render
from django.contrib.auth import get_user_model

from django_tables2 import RequestConfig

from .tables import SetTable
from workout.models import Set


def ladder(request, search=None):
    queryset = Set.objects.all()
    table = SetTable(queryset)
    RequestConfig(request).configure(table)

    return render(request, 'ladder/ladder.html',{
        'table': table
        })
