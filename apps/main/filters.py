import django_filters 
from apps.main.models import HomePage


class HomePageFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = HomePage
        fields = ['title', 'description']

    # @property
    # def qs(self):
    #     if not hasattr(self, '_qs'):
    #         qs = self.queryset.all()
    #         if self.is_bound:
    #             if len(self.errors) > 0:
    #                 raise Exception(self.errors)
    #             qs = self.filter_queryset(qs)
    #         self._qs = qs
    #     return self._qs