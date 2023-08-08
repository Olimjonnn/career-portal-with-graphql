import django_filters
from apps.blog.models import Blog
from graphene_django_filter import AdvancedDjangoFilterConnectionField, AdvancedFilterSet

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ['title']
            
        
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

