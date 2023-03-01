import django_filters
from .models import Roommset




class RoommsetFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='lte')
    class Meta:
        model = Roommset
        fields = ['title','place', 'price','gender']