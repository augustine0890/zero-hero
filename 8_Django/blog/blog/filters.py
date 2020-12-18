from django_filters import rest_framework as filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import Post

class PostFilter(filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte', label="Start Date")
    end_date = DateFilter(field_name="date", lookup_expr='lte', label="End Date")
    title = CharFilter(field_name='title', lookup_expr='icontains', label="Title")
    
    class Meta:
        model = Post
        fields = ['title', 'start_date', 'end_date']














