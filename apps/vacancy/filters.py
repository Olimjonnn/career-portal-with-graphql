
import django_filters
from apps.vacancy.models import Vacancy

class VacancyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    # tags__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = ['title', 'description']



    