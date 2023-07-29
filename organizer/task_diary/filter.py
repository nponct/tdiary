from django_filters  import rest_framework as filters
from .models import Tasks

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    created = filters.RangeFilter()

    class Meta:
        model = Tasks
        fields = ['title','created']